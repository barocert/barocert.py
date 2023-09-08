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


class PasscertServiceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.passcertService = PasscertService('TESTER', 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I=')
        self.passcertService.IPRestrictOnOff = True
        self.passcertService.UseStaticIP = False
        self.passcertService.UseLocalTimeYN = True
        
        self.clientCode = "023070000014"
        
    # # 본인인증 요청
    # def test_requestIdentity(self):
    #     identity = PassIdentity(        
    #         receiverHP = self.passcertService._encrypt('01067668440'),
    #         receiverName = self.passcertService._encrypt('정우석'),
    #         receiverBirthday = self.passcertService._encrypt('19900911'),
    #         reqTitle = '본인인증 요청 메시지 제목란',
    #         reqMessage = self.passcertService._encrypt('본인인증 요청 메시지'),
    #         callCenterNum = '1600-9854',
    #         expireIn = 1000,
    #         token = self.passcertService._encrypt('본인인증요청토큰'),
    #         userAgreementYN = True,
    #         receiverInfoYN = True,
    #         appUseYN = False
    #     )

    #     try :
    #         obj = self.passcertService.requestIdentity(self.clientCode, identity)
    #         print(obj.receiptId)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 본인인증 상태확인            
    # def test_getIdentityStatus(self) :
    #     try :
    #         obj = self.passcertService.getIdentityStatus(self.clientCode, '02309080230700000140000000000007')
    #         print(obj.clientCode)
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.reqMessage)
    #         print(obj.requestDT)
    #         print(obj.completeDT)
    #         print(obj.expireDT)
    #         print(obj.rejectDT)
    #         print(obj.tokenType)
    #         print(obj.userAgreementYN)
    #         print(obj.receiverInfoYN)
    #         print(obj.telcoType)
    #         print(obj.deviceOSType)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 본인인증 검증            
    # def test_verifyIdentity(self) :
    #     identityVerify = PassIdentityVerify(        
    #         receiverHP = self.passcertService._encrypt('01067668440'),
    #         receiverName = self.passcertService._encrypt('정우석')
    #     )

    #     try :
    #         obj = self.passcertService.verifyIdentity(self.clientCode, '02309080230700000140000000000007', identityVerify)
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.receiverName)
    #         print(obj.receiverYear)
    #         print(obj.receiverDay)
    #         print(obj.receiverGender)
    #         print(obj.receiverForeign)
    #         print(obj.receiverTelcoType)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
    
    # # 전자서명 요청
    # def test_requestSign(self):
    #     sign = PassSign(        
    #         receiverHP = self.passcertService._encrypt('01067668440'),
    #         receiverName = self.passcertService._encrypt('정우석'),
    #         receiverBirthday = self.passcertService._encrypt('19900911'),
    #         reqTitle = '전자서명 요청 메시지 제목란',
    #         reqMessage = self.passcertService._encrypt('전자서명 요청 메시지'),
    #         callCenterNum = '1600-9854',
    #         expireIn = 1000,
    #         token = self.passcertService._encrypt('전자서명테스트데이터'),
    #         tokenType = 'HASH',
    #         userAgreementYN = True,
    #         receiverInfoYN = True,
    #         originalTypeCode = 'AG',
    #         originalURL = 'https://www.passcert.co.kr',
    #         originalFormatCode = 'HTML',
    #         appUseYN = False,
    #     )
        
    #     try :
    #         obj = self.passcertService.requestSign(self.clientCode, sign)
    #         print(obj.receiptId)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # def test_getSignState(self) :
    #     try :
    #         obj = self.passcertService.getSignStatus(self.clientCode, '02309080230700000140000000000012')
    #         print(obj.clientCode)
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.reqMessage)
    #         print(obj.requestDT)
    #         print(obj.completeDT)
    #         print(obj.expireDT)
    #         print(obj.rejectDT)
    #         print(obj.tokenType)
    #         print(obj.userAgreementYN)
    #         print(obj.receiverInfoYN)
    #         print(obj.telcoType)
    #         print(obj.deviceOSType)
    #         print(obj.originalTypeCode)
    #         print(obj.originalURL)
    #         print(obj.originalFormatCode)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # def test_verifySign(self) :
    #     signVerify = PassSignVerify(        
    #         receiverHP = self.passcertService._encrypt('01067668440'),
    #         receiverName = self.passcertService._encrypt('정우석')
    #     )
        
    #     try :
    #         obj = self.passcertService.verifySign(self.clientCode, '02309080230700000140000000000012', signVerify)
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.receiverName)
    #         print(obj.receiverHP)
    #         print(obj.receiverYear)
    #         print(obj.receiverDay)
    #         print(obj.receiverGender)
    #         print(obj.receiverForeign)
    #         print(obj.receiverTelcoType)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)

    # # 자동이체 출금동의 요청           
    # def test_requestCMS(self):
    #     cms = PassCMS(        
    #         receiverHP = self.passcertService._encrypt('01067668440'),
    #         receiverName = self.passcertService._encrypt('정우석'),
    #         receiverBirthday = self.passcertService._encrypt('19900911'),
    #         reqTitle = '출금동의 요청 메시지 제목란',
    #         reqMessage = self.passcertService._encrypt('출금동의 요청 메시지'),
    #         callCenterNum = '1600-9854',
    #         expireIn = 1000,
    #         userAgreementYN = True,
    #         receiverInfoYN = True,
    #         bankName = self.passcertService._encrypt('국민은행'),
    #         bankAccountNum = self.passcertService._encrypt('19-******-1231'),
    #         bankAccountName = self.passcertService._encrypt('홍길동'),
    #         bankServiceType = self.passcertService._encrypt('CMS'),
    #         bankWithdraw = self.passcertService._encrypt('1,000,000원'),
    #         appUseYN = False,
    #     )
        
    #     try :
    #         obj = self.passcertService.requestCMS(self.clientCode, cms)
    #         print(obj.receiptId)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 자동이체 출금동의 상태확인            
    # def test_getCMSStatus(self) :
    #     try :
    #         obj = self.passcertService.getCMSStatus(self.clientCode, '02309080230700000140000000000016')
    #         print(obj.clientCode)
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.reqMessage)
    #         print(obj.requestDT)
    #         print(obj.completeDT)
    #         print(obj.expireDT)
    #         print(obj.rejectDT)
    #         print(obj.tokenType)
    #         print(obj.userAgreementYN)
    #         print(obj.receiverInfoYN)
    #         print(obj.telcoType)
    #         print(obj.deviceOSType)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 자동이체 출금동의 검증            
    # def test_verifyCMS(self) :
    #     cmsVerify = PassCMSVerify(        
    #         receiverHP = self.passcertService._encrypt('01067668440'),
    #         receiverName = self.passcertService._encrypt('정우석')
    #     )
        
    #     try :
    #         obj = self.passcertService.verifyCMS(self.clientCode, '02309080230700000140000000000016', cmsVerify)
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.receiverName)
    #         print(obj.receiverHP)
    #         print(obj.receiverYear)
    #         print(obj.receiverDay)
    #         print(obj.receiverGender)
    #         print(obj.receiverForeign)
    #         print(obj.receiverTelcoType)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)

    # # 간편로그인 요청
    # def test_requestLogin(self):
    #     login = PassLogin(        
    #         receiverHP = self.passcertService._encrypt('01067668440'),
    #         receiverName = self.passcertService._encrypt('정우석'),
    #         receiverBirthday = self.passcertService._encrypt('19900911'),
    #         reqTitle = '간편로그인 요청 메시지 제목란',
    #         reqMessage = self.passcertService._encrypt('간편로그인 요청 메시지'),
    #         callCenterNum = '1600-9854',
    #         expireIn = 1000,
    #         token = self.passcertService._encrypt('간편로그인요청토큰'),
    #         userAgreementYN = True,
    #         receiverInfoYN = True,
    #         appUseYN = False
    #     )
        
    #     try :
    #         obj = self.passcertService.requestLogin(self.clientCode, login)
    #         print(obj.receiptId)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 간편로그인 상태확인            
    # def test_getLoginStatus(self) :
    #     try :
    #         obj = self.passcertService.getLoginStatus(self.clientCode, '02309080230700000140000000000020')
    #         print(obj.clientCode)
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.reqMessage)
    #         print(obj.requestDT)
    #         print(obj.completeDT)
    #         print(obj.expireDT)
    #         print(obj.rejectDT)
    #         print(obj.tokenType)
    #         print(obj.userAgreementYN)
    #         print(obj.receiverInfoYN)
    #         print(obj.telcoType)
    #         print(obj.deviceOSType)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # # 간편로그인 검증            
    # def test_verifyLogin(self) :
    #     loginVerify = PassLoginVerify(        
    #         receiverHP = self.passcertService._encrypt('01067668440'),
    #         receiverName = self.passcertService._encrypt('정우석')
    #     )

    #     try :
    #         obj = self.passcertService.verifyLogin(self.clientCode, '02309080230700000140000000000020', loginVerify)
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.receiverName)
    #         print(obj.receiverYear)
    #         print(obj.receiverDay)
    #         print(obj.receiverGender)
    #         print(obj.receiverForeign)
    #         print(obj.receiverTelcoType)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PasscertServiceTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
