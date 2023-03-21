# -*- coding: utf-8 -*-
# Module for KakaocertService API. It include base functionality of the
# RESTful web service request and parse json result. It uses Linkhub module
# to accomplish authentication APIs.
#
# 
# Author : 
# Written : 2023-03-08
# Updated : 2023-03-08
# Thanks for your interest.

import json
import zlib
import base64
import hmac
import json

from io import BytesIO
from hashlib import sha256
from time import time as stime
from json import JSONEncoder
from collections import namedtuple


try:
    import http.client as httpclient
except ImportError:
    import httplib as httpclient

import linkhub
from linkhub import LinkhubException

ServiceID = 'BAROCERT'
ServiceURL = 'bc-api.linkhub.kr/KAKAO' # TODO :: 나중에 바꿔야 함.
ServiceURL_Static = 'static-barocert.linkhub.co.kr'
ServiceURL_GA = 'ga-barocert.linkhub.co.kr'
APIVersion = '2.0'


def __with_metaclass(meta, *bases):
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

    return type.__new__(metaclass, 'temporary_class', (), {})


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class KakaocertService(__with_metaclass(Singleton, object)):
    IsTest = False
    IPRestrictOnOff = True
    UseStaticIP = False
    UseGAIP = False
    UseLocalTimeYN = True

    def __init__(self, LinkID, SecretKey, timeOut=15):
        """ 생성자.
            args
                LinkID : 링크허브에서 발급받은 LinkID
                SecretKey : 링크허브에서 발급받은 SecretKey
        """
        self.__linkID = LinkID
        self.__secretKey = SecretKey
        self.__scopes = ["partner","401","402","403","404"]
        self.__tokenCache = {}
        self.__conn = None
        self.__connectedAt = stime()
        self.__timeOut = timeOut

    def _getConn(self):
        if stime() - self.__connectedAt >= self.__timeOut or self.__conn == None:
            if self.UseGAIP :
                self.__conn = httpclient.HTTPSConnection(ServiceURL_GA)
            elif self.UseStaticIP :
                self.__conn = httpclient.HTTPSConnection(ServiceURL_Static)
            else :
                self.__conn = httpclient.HTTPSConnection(ServiceURL)

            self.__connectedAt = stime()
            return self.__conn
        else:
            return self.__conn

    def _getToken(self, ClientCode):

        try:
            token = self.__tokenCache[ClientCode]
        except KeyError:
            token = None

        refreshToken = True

        if token != None:
            refreshToken = token.expiration[:-5] < linkhub.getTime(self.UseStaticIP, self.UseLocalTimeYN, self.UseGAIP)

        if refreshToken:
            try:
                token = linkhub.generateToken(self.__linkID, self.__secretKey,
                                              ServiceID, ClientCode, self.__scopes, None if self.IPRestrictOnOff else "*",
                                              self.UseStaticIP, self.UseLocalTimeYN, self.UseGAIP)

                try:
                    del self.__tokenCache[ClientCode]
                except KeyError:
                    pass

                self.__tokenCache[ClientCode] = token

            except LinkhubException as LE:
                raise BarocertException(LE.code, LE.message)

        return token

    def _httpget(self, url, ClientCode=None, UserID=None):

        conn = self._getConn()

        headers = {"x-pb-version": APIVersion}

        if ClientCode != None:
            headers["Authorization"] = "Bearer " + self._getToken(ClientCode).session_token

        headers["Accept-Encoding"] = "gzip,deflate"

        conn.request('GET', url, '', headers)

        response = conn.getresponse()
        responseString = response.read()

        if Utils.isGzip(response, responseString):
            responseString = Utils.gzipDecomp(responseString)

        if response.status != 200:
            err = Utils.json2obj(responseString)
            raise BarocertException(int(err.code), err.message)
        else:
            return Utils.json2obj(responseString)

    def _httppost(self, url, postData, ClientCode=None, UserID=None, ActionOverride=None, contentsType=None):

        callDT = linkhub.getTime(self.UseStaticIP, False, self.UseGAIP)

        hmacTarget = ""
        hmacTarget += "POST\n"
        hmacTarget += Utils.b64_sha256(postData) + "\n"
        hmacTarget += callDT + "\n"
        hmacTarget += APIVersion + "\n"

        hmac = Utils.b64_hmac_sha256(self.__secretKey, hmacTarget)

        conn = self._getConn()

        headers = {"x-lh-date": callDT}
        headers["x-lh-version"] = APIVersion
        headers["Authorization"] = "Bearer " + self._getToken(ClientCode).session_token
        headers["Content-Type"] = "application/json; charset=utf8"
        headers["Accept-Encoding"] = "gzip,deflate"
        headers["x-bc-auth"] = self.__linkID + ' ' +hmac

        conn.request('POST', url, postData, headers)

        response = conn.getresponse()
        responseString = response.read()

        if Utils.isGzip(response, responseString):
            responseString = Utils.gzipDecomp(responseString)

        if response.status != 200:
            err = Utils.json2obj(responseString)
            raise BarocertException(int(err.code), err.message)
        else:
            return Utils.json2obj(responseString)

    def _parse(self, jsonString):
        return Utils.json2obj(jsonString)

    def _stringtify(self, obj):
        return json.dumps(obj, cls=KakaocertEncoder)

    # 전자서명 요청(단건)
    def requestESign(self, ClientCode, requestESign, appUseYN = False):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if requestESign == None or requestESign == "":
            raise BarocertException(-99999999, "전자서명 요청정보가 입력되지 않았습니다.")

        requestESign.clientCode = ClientCode
        requestESign.appUseYN = appUseYN

        postData = self._stringtify(requestESign)

        return self._httppost('/KAKAO/ESign/Request', postData, ClientCode, "", "")

    # 전자서명 요청(다건)
    def bulkRequestESign(self, ClientCode, requestESign, appUseYN = False):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if requestESign == None or requestESign == "":
            raise BarocertException(-99999999, "전자서명 요청정보가 입력되지 않았습니다.")

        requestESign.clientCode = ClientCode
        requestESign.appUseYN = appUseYN

        postData = self._stringtify(requestESign)

        return self._httppost('/KAKAO/ESign/BulkRequest', postData, ClientCode, "", "")

    # 전자서명 상태확인(단건)
    def getESignState(self, ClientCode, receiptId):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if receiptId == None or receiptId == "":
            raise BarocertException(-99999999, "접수아이디가 입력되지 않았습니다.")

        return self._httpget('/KAKAO/ESign/Status/' + ClientCode + '/' + receiptId, ClientCode)

    # 전자서명 상태확인(다건)	
    def getBulkESignState(self, ClientCode, receiptId):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if receiptId == None or receiptId == "":
            raise BarocertException(-99999999, "접수아이디가 입력되지 않았습니다.")

        return self._httpget('/KAKAO/ESign/BulkStatus/' + ClientCode + '/' + receiptId, ClientCode)

    # 전자서명 검증(단건)
    def verifyESign(self, ClientCode, receiptId):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if receiptId == None or receiptId == "":
            raise BarocertException(-99999999, "접수아이디가 입력되지 않았습니다.")
        
        postData = self._stringtify({
            "clientCode": ClientCode,
            "receiptId": receiptId
        })

        return self._httppost('/KAKAO/ESign/Verify', postData, ClientCode, "", "")

    # 전자서명 검증(다건)
    def bulkverifyESign(self, ClientCode, receiptId):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if receiptId == None or receiptId == "":
            raise BarocertException(-99999999, "접수아이디가 입력되지 않았습니다.")
        
        postData = self._stringtify({
            "clientCode": ClientCode,
            "receiptId": receiptId
        })

        return self._httppost('/KAKAO/ESign/BulkVerify', postData, ClientCode, "", "")

    # 본인인증 요청
    def requestVerifyAuth(self, ClientCode, requestVerifyAuth, appUseYN = False):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if requestVerifyAuth == None or requestVerifyAuth == "":
            raise BarocertException(-99999999, "본인인증 요청정보가 입력되지 않았습니다.")

        requestVerifyAuth.clientCode = ClientCode
        requestVerifyAuth.appUseYN = appUseYN

        postData = self._stringtify(requestVerifyAuth)

        return self._httppost('/KAKAO/VerifyAuth/Request', postData, ClientCode, "", "")

    # 전자서명 상태확인
    def getVerifyAuthState(self, ClientCode, receiptId):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if receiptId == None or receiptId == "":
            raise BarocertException(-99999999, "접수아이디가 입력되지 않았습니다.")

        return self._httpget('/KAKAO/VerifyAuth/Status/' + ClientCode + '/' + receiptId , ClientCode)
    
    # 본인인증 검증
    def verifyAuth(self, ClientCode, receiptId):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if receiptId == None or receiptId == "":
            raise BarocertException(-99999999, "접수아이디가 입력되지 않았습니다.")

        return self._httpget('/KAKAO/VerifyAuth/Verify/' + receiptId , ClientCode)

    # 출금동의 요청
    def requestCMS(self, ClientCode, requestCMS, appUseYN = False):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if requestCMS == None or requestCMS == "":
            raise BarocertException(-99999999, "자동이체 출금동의 요청정보가 입력되지 않았습니다.")

        requestCMS.clientCode = ClientCode
        requestCMS.isAppUseYN = appUseYN

        postData = self._stringtify(requestCMS)

        return self._httppost('/KAKAO/CMS/Request', postData, ClientCode, "", "")

    # 출금동의 상태확인
    def getCMSState(self, ClientCode, receiptId):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if receiptId == None or receiptId == "":
            raise BarocertException(-99999999, "접수아이디가 입력되지 않았습니다.")

        return self._httpget('/KAKAO/CMS/Status/' + ClientCode + '/' + receiptId , ClientCode)

    # 출금동의 검증
    def verifyCMS(self, ClientCode, receiptId):

        if ClientCode not in self.__ClientCode:
            raise BarocertException(-99999999, "이용기관코드가 입력되지 않았습니다.")
        if receiptId == None or receiptId == "":
            raise BarocertException(-99999999, "접수아이디가 입력되지 않았습니다.")

        postData = self._stringtify({
            "clientCode": ClientCode,
            "receiptId": receiptId
        })

        return self._httppost('/KAKAO/CMS/Verify', postData, ClientCode, "", "")


class BarocertException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

class KakaocertEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class JsonObject(object):
    def __init__(self, dic):
        try:
            d = dic.__dict__
        except AttributeError:
            d = dic._asdict()

        self.__dict__.update(d)

    def __getattr__(self, name):
        return None

class Utils:
    @staticmethod
    def b64_sha256(input):
        return base64.b64encode(sha256(input.encode('utf-8')).digest()).decode('utf-8')

    @staticmethod
    def b64_hmac_sha256(keyString, targetString):
        return base64.b64encode(hmac.new(base64.b64decode(keyString.encode('utf-8')), targetString.encode('utf-8'), sha256).digest()).decode('utf-8').rstrip('\n')

    @staticmethod
    def _json_object_hook(d):
        return JsonObject(namedtuple('JsonObject', d.keys())(*d.values()))

    @staticmethod
    def json2obj(data):
        if (type(data) is bytes): data = data.decode('utf-8')
        return json.loads(data, object_hook=Utils._json_object_hook)

    @staticmethod
    def isGzip(response, data):
        if (response.getheader('Content-Encoding') != None and
                'gzip' in response.getheader('Content-Encoding')):
            return True
        else:
            return False

    @staticmethod
    def gzipDecomp(data):
        return zlib.decompress(data, 16 + zlib.MAX_WBITS)
