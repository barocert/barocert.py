# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
import random

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

try:
    import unittest2 as unittest
except ImportError:
    import unittest
from datetime import datetime
from barocert import *


class KakaocertServiceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.kakaocertService = KakaocertService('TESTER', 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I=')
        self.kakaocertService.IPRestrictOnOff = True
        self.kakaocertService.UseStaticIP = False
        
        self.clientCode = "023040000001"

    # # 본인인증 요청
    # def test_requestIdentity(self):
    #     identity = KakaoIdentity(        
    #         receiverHP = self.kakaocertService._encrypt('01012341234'),
    #         receiverName = self.kakaocertService._encrypt('홍길동'),
    #         receiverBirthday = self.kakaocertService._encrypt('19700101'),
    #         reqTitle = '본인인증 요청 메시지 제목',
    #         expireIn = 1000,
    #         token = self.kakaocertService._encrypt('본인인증 요청 원문'),
    #         appUseYN = False,
    #         returnURL = 'https://kakao.barocert.com',
    #     )
        
    #     try :
    #         obj = self.kakaocertService.requestIdentity(self.clientCode, identity)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)

    # # 본인인증 상태확인        
    # def test_getIdentityStatus(self) :
    #     try :
    #         obj = self.kakaocertService.getIdentityStatus(self.clientCode, '02309080230400000010000000000005')
    #         print(obj.receiptID)
    #         print(obj.clientCode)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.authCategory)
    #         print(obj.returnURL)
    #         print(obj.requestDT)
    #         print(obj.viewDT)
    #         print(obj.completeDT)
    #         print(obj.expireDT)
    #         print(obj.verifyDT)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 본인인증 검증            
    # def test_verifyIdentity(self) :
    #     try :
    #         obj = self.kakaocertService.verifyIdentity(self.clientCode, '02309080230400000010000000000002')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
    
    # # 전자서명(단건) 요청
    # def test_requestSign(self):
    #     sign = KakaoSign(        
    #         receiverHP = self.kakaocertService._encrypt('01012341234'),
    #         receiverName = self.kakaocertService._encrypt('홍길동'),
    #         receiverBirthday = self.kakaocertService._encrypt('19700101'),
    #         reqTitle = '전자서명(단건) 요청 메시지 제목',
    #         expireIn = 1000,
    #         token = self.kakaocertService._encrypt('전자서명(단건) 요청 원문'),
    #         tokenType = 'TEXT',
    #         appUseYN = False,
    #         returnURL = 'https://kakao.barocert.com'
    #     )
        
    #     try :
    #         obj = self.kakaocertService.requestSign(self.clientCode, sign)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 전자서명(단건) 상태확인            
    # def test_getSignState(self) :
    #     try :
    #         obj = self.kakaocertService.getSignStatus(self.clientCode, '02309080230400000010000000000006')
    #         print(obj.receiptID)
    #         print(obj.clientCode)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.authCategory)
    #         print(obj.returnURL)
    #         print(obj.requestDT)
    #         print(obj.viewDT)
    #         print(obj.completeDT)
    #         print(obj.expireDT)
    #         print(obj.verifyDT)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 전자서명(단건) 검증            
    # def test_verifySign(self) :
    #     try :
    #         obj = self.kakaocertService.verifySign(self.clientCode, '02309080230400000010000000000006')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 전자서명(복수) 요청
    # def test_requestMultiSign(self):
        
    #     multiSignTokens = []
    #     for x in range(0,5):
    #         multiSignTokens.append(
    #             KakaoMultiSignTokens(
    #                 reqTitle = "전자서명(복수) 요청 메시지 제목" + str(x),
    #                 token = self.kakaocertService._encrypt("전자서명(복수) 요청 원문" + str(x)) 
    #             )
    #         )    
        
    #     multiSign = KakaoMultiSign(        
    #         receiverHP = self.kakaocertService._encrypt('01012341234'),
    #         receiverName = self.kakaocertService._encrypt('홍길동'),
    #         receiverBirthday = self.kakaocertService._encrypt('19700101'),
    #         reqTitle = '전자서명(복수) 요청 메시지 제목',
    #         expireIn = 1000,
    #         tokens = multiSignTokens,
    #         tokenType = 'TEXT',
    #         appUseYN = False,
    #         returnURL = 'https://kakao.barocert.com'
    #     )
        
    #     try :
    #         obj = self.kakaocertService.requestMultiSign(self.clientCode, multiSign)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 전자서명(복수) 상태확인            
    # def test_getMultiSignState(self) :
    #     try :
    #         obj = self.kakaocertService.getMultiSignStatus(self.clientCode, '02309080230400000010000000000011')
    #         print(obj.receiptID)
    #         print(obj.clientCode)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.authCategory)
    #         print(obj.returnURL)
    #         print(obj.requestDT)
    #         print(obj.viewDT)
    #         print(obj.completeDT)
    #         print(obj.expireDT)
    #         print(obj.verifyDT)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)

    # # 전자서명(복수) 검증            
    # def test_verifyMultiSign(self) :
    #     try :
    #         obj = self.kakaocertService.verifyMultiSign(self.clientCode, '02309080230400000010000000000011')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         for multiSignedData in obj.multiSignedData:
    #             print(multiSignedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)

    # # 자동이체 출금동의 요청
    # def test_requestCMS(self):
    #     cms = KakaoCMS(        
    #         receiverHP = self.kakaocertService._encrypt('01012341234'),
    #         receiverName = self.kakaocertService._encrypt('홍길동'),
    #         receiverBirthday = self.kakaocertService._encrypt('19700101'),
    #         reqTitle = '출금동의 요청 메시지 제목',
    #         expireIn = 1000,
    #         requestCorp = self.kakaocertService._encrypt("링크허브"),
    #         bankName = self.kakaocertService._encrypt("국민은행"),
    #         bankAccountNum = self.kakaocertService._encrypt("19-321442-1231"),
    #         bankAccountName = self.kakaocertService._encrypt("홍길동"),
    #         bankAccountBirthday = self.kakaocertService._encrypt("19700101"),
    #         bankServiceType = self.kakaocertService._encrypt("CMS"),
    #         appUseYN = False,
    #         returnURL = 'https://kakao.barocert.com'
    #     )
        
    #     try :
    #         obj = self.kakaocertService.requestCMS(self.clientCode, cms)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 자동이체 출금동의 상태확인            
    # def test_getCMSStatus(self) :
    #     try :
    #         obj = self.kakaocertService.getCMSStatus(self.clientCode, '02309080230400000010000000000013')
    #         print(obj.receiptID)
    #         print(obj.clientCode)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.authCategory)
    #         print(obj.returnURL)
    #         print(obj.requestDT)
    #         print(obj.viewDT)
    #         print(obj.completeDT)
    #         print(obj.expireDT)
    #         print(obj.verifyDT)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 자동이체 출금동의 검증            
    # def test_verifyCMS(self) :
    #     try :
    #         obj = self.kakaocertService.verifyCMS(self.clientCode, '02309080230400000010000000000013')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)

    # # 간편로그인 검증            
    # def test_verifyLogin(self) :
    #     try :
    #         obj = self.kakaocertService.verifyLogin(self.clientCode, '019e25d799-e7b0-4aa0-9d7c-b33f526972b3')
    #         print(obj.txID)
    #         print(obj.state)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)            


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KakaocertServiceTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
