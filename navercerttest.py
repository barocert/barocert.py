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


# class NavercertServiceTestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(self):
#         self.navercertService = NavercertService('TESTER', 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I=')
#         self.navercertService.IPRestrictOnOff = True
#         self.navercertService.UseLocalTimeYN = True
#         self.navercertService.UseStaticIP = False
        
#         self.clientCode = "023090000021"

    # 본인인증 요청
    # def test_requestIdentity(self):
    #     identity = NaverIdentity(        
    #         receiverHP = self.navercertService._encrypt('01012341234'),
    #         receiverName = self.navercertService._encrypt('홍길동'),
    #         receiverBirthday = self.navercertService._encrypt('19700101'),
    #         callCenterNum = '1588-1600',
    #         expireIn = 1000,
    #         appUseYN = False,
    #         returnURL = 'navercert://Sign',
    #     )
        
    #     try :
    #         obj = self.navercertService.requestIdentity(self.clientCode, identity)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)

    # 본인인증 상태확인        
    # def test_getIdentityStatus(self) :
    #     try :
    #         obj = self.navercertService.getIdentityStatus(self.clientCode, '02310310230900000210000000000001')
    #         print(obj.receiptID)
    #         print(obj.clientCode)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.deviceOSType)
    #         print(obj.returnURL)
    #         print(obj.expireDT)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # 본인인증 검증            
    # def test_verifyIdentity(self) :
    #     try :
    #         obj = self.navercertService.verifyIdentity(self.clientCode, '02310310230900000210000000000001')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.signedData)
    #         print(obj.ci)
    #         print(obj.receiverName)
    #         print(obj.receiverDay)
    #         print(obj.receiverYear)
    #         print(obj.receiverHP)
    #         print(obj.receiverGender)
    #         print(obj.receiverEmail)
    #         print(obj.receiverForeign)

    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
    
    # 전자서명(단건) 요청
    # def test_requestSign(self):
    #     sign = NaverSign(        
    #         receiverHP = self.navercertService._encrypt('01012341234'),
    #         receiverName = self.navercertService._encrypt('홍길동'),
    #         receiverBirthday = self.navercertService._encrypt('19700101'),
    #         reqTitle = '인증요청 메시지 제목란',
    #         reqMessage = self.navercertService._encrypt('전자서명 메시지'),
    #         callCenterNum = '1588-1600',
    #         expireIn = 1000,
    #         token = self.navercertService._encrypt('전자서명단건테스트데이터'),
    #         tokenType = 'TEXT',
    #         appUseYN = False,
    #         returnURL = 'navercert://Sign'
    #     )
        
    #     try :
    #         obj = self.navercertService.requestSign(self.clientCode, sign)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # 전자서명(단건) 상태확인            
    # def test_getSignState(self) :
    #     try :
    #         obj = self.navercertService.getSignStatus(self.clientCode, '02310310230900000210000000000002')
    #         print(obj.receiptID)
    #         print(obj.clientCode)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.tokenType)
    #         print(obj.deviceOSType)
    #         print(obj.returnURL)
    #         print(obj.expireDT)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # 전자서명(단건) 검증            
    # def test_verifySign(self) :
    #     try :
    #         obj = self.navercertService.verifySign(self.clientCode, '02310310230900000210000000000002')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.signedData)
    #         print(obj.ci)
    #         print(obj.receiverName)
    #         print(obj.receiverDay)
    #         print(obj.receiverYear)
    #         print(obj.receiverHP)
    #         print(obj.receiverGender)
    #         print(obj.receiverEmail)
    #         print(obj.receiverForeign)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # 전자서명(복수) 요청
    # def test_requestMultiSign(self):
        
    #     multiSignTokens = []
    #     for x in range(0,5):
    #         multiSignTokens.append(
    #             NaverMultiSignTokens(
    #                 token = self.navercertService._encrypt("전자서명복수테스트데이터" + str(x)),
    #                 tokenType = "TEXT",
    #             )
    #         )    
        
    #     multiSign = NaverMultiSign(        
    #         receiverHP = self.navercertService._encrypt('01012341234'),
    #         receiverName = self.navercertService._encrypt('홍길동'),
    #         receiverBirthday = self.navercertService._encrypt('19700101'),
    #         reqTitle = '인증요청 메시지 제목란',
    #         reqMessage = self.navercertService._encrypt('인증요청 메시지'),
    #         callCenterNum = '1588-1600',
    #         expireIn = 1000,
    #         tokens = multiSignTokens,
    #         appUseYN = False,
    #         returnURL = 'navercert://Sign'
    #     )
        
    #     try :
    #         obj = self.navercertService.requestMultiSign(self.clientCode, multiSign)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # 전자서명(복수) 상태확인            
    # def test_getMultiSignState(self) :
    #     try :
    #         obj = self.navercertService.getMultiSignStatus(self.clientCode, '02310310230900000210000000000003')
    #         print(obj.receiptID)
    #         print(obj.clientCode)
    #         print(obj.state)
    #         print(obj.expireIn)
    #         print(obj.callCenterName)
    #         print(obj.callCenterNum)
    #         print(obj.reqTitle)
    #         print(obj.tokenTypes)
    #         print(obj.deviceOSType)
    #         print(obj.returnURL)
    #         print(obj.expireDT)
    #         print(obj.scheme)
    #         print(obj.appUseYN)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)

    # 전자서명(복수) 검증            
    # def test_verifyMultiSign(self) :
    #     try :
    #         obj = self.navercertService.verifyMultiSign(self.clientCode, '02310310230900000210000000000003')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         for multiSignedData in obj.multiSignedData:
    #             print(multiSignedData)
    #         print(obj.ci)
    #         print(obj.receiverName)
    #         print(obj.receiverDay)
    #         print(obj.receiverYear)
    #         print(obj.receiverHP)
    #         print(obj.receiverGender)
    #         print(obj.receiverEmail)
    #         print(obj.receiverForeign)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)

# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(NavercertServiceTestCase)
#     unittest.TextTestRunner(verbosity=2).run(suite)