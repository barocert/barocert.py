# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
# import imp
import random

# imp.reload(sys)
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


class NavercertServiceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.navercertService = NavercertService('TESTER', 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I=')
        self.navercertService.IPRestrictOnOff = True
        self.navercertService.UseStaticIP = False
        
        self.clientCode = "023090000021"

    # 본인인증 요청
    # def test_requestIdentity(self):
    #     identity = NaverIdentity(        
    #         receiverHP = self.navercertService._encrypt('01012341234'),
    #         receiverName = self.navercertService._encrypt('홍길동'),
    #         receiverBirthday = self.navercertService._encrypt('19700101'),
    #         callCenterNum = '1588-1600',
    #         expireIn = 1000,
    #         appUseYN = False,
    #         deviceOSType = 'IOS',
    #         returnURL = 'navercert://Identity',
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
    #         print(obj.expireDT)
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
    
    # file = open("./barocert.pdf", 'rb')
    # target = file.read()
    # file.close()
    
    # 전자서명(단건) 요청
    # def test_requestSign(self):
    #     sign = NaverSign(        
    #         receiverHP = self.navercertService._encrypt('01012341234'),
    #         receiverName = self.navercertService._encrypt('홍길동'),
    #         receiverBirthday = self.navercertService._encrypt('19700101'),
    #         reqTitle = '전자서명(단건) 요청 메시지 제목',
    #         reqMessage = self.navercertService._encrypt('전자서명(단건) 요청 메시지'),
    #         callCenterNum = '1588-1600',
    #         expireIn = 1000,
    #         tokenType = 'TEXT',
    #         token = self.navercertService._encrypt('전자서명(단건) 요청 원문'),
    #         # tokenType = 'PDF',
    #         # token = self.navercertService._encrypt(self.navercertService._sha256_base64url_file(self.target)),
    #         appUseYN = False,
    #         deviceOSType = 'IOS',
    #         returnURL = 'navercert://Sign'
    #     )
        
        # try :
        #     obj = self.navercertService.requestSign(self.clientCode, sign)
        #     print(obj.receiptID)
        # except BarocertException as BE :
        #     print(BE.code)
        #     print(BE.message)
            
    # 전자서명(단건) 상태확인            
    # def test_getSignState(self) :
    #     try :
    #         obj = self.navercertService.getSignStatus(self.clientCode, '02310310230900000210000000000002')
    #         print(obj.receiptID)
    #         print(obj.clientCode)
    #         print(obj.state)
    #         print(obj.expireDT)
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
    #                 tokenType = "TEXT",    
    #                 token = self.navercertService._encrypt("전자서명(복수) 요청 원문" + str(x)),
    # #               tokenType = 'HASH',
    # #               token = self.navercertService._encrypt(self.navercertService._sha256_base64url("전자서명(복수) 요청 원문" + str(x))),
    #             )
    #         )    
        
    #     multiSign = NaverMultiSign(        
    #         receiverHP = self.navercertService._encrypt('01012341234'),
    #         receiverName = self.navercertService._encrypt('홍길동'),
    #         receiverBirthday = self.navercertService._encrypt('19700101'),
    #         reqTitle = '전자서명(복수) 요청 메시지 제목',
    #         reqMessage = self.navercertService._encrypt('전자서명(복수) 요청 메시지'),
    #         callCenterNum = '1588-1600',
    #         expireIn = 1000,
    #         tokens = multiSignTokens,
    #         appUseYN = False,
    #         deviceOSType = 'IOS',
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
    #         print(obj.expireDT)
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

    # 출금동의 요청
    # def test_requestCMS(self):
    #     cms = NaverCMS(        
    #         receiverHP = self.navercertService._encrypt('01012341234'),
    #         receiverName = self.navercertService._encrypt('홍길동'),
    #         receiverBirthday = self.navercertService._encrypt('19700101'),
    #         reqTitle = '출금동의 요청 메시지 제목',
    #         reqMessage = self.navercertService._encrypt('출금동의 요청 메시지'),
    #         callCenterNum = '1588-1600',
    #         expireIn = 1000,
    #         requestCorp = self.navercertService._encrypt('청구기관'),    
    #         bankName = self.navercertService._encrypt('출금은행'),    
    #         bankAccountNum = self.navercertService._encrypt('123-456-7890'),    
    #         bankAccountName = self.navercertService._encrypt('홍길동'),    
    #         bankAccountBirthday = self.navercertService._encrypt('19700101'),    
    #         appUseYN = False,
    #         deviceOSType = 'IOS',
    #         returnURL = 'navercert://cms',
    #     )
    
    #     try :
    #         obj = self.navercertService.requestCMS(self.clientCode, cms)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)

    # 출금동의 상태확인        
    # def test_getCMSStatus(self) :
    #     try :
    #         obj = self.navercertService.getCMSStatus(self.clientCode, '02310310230900000210000000000001')
    #         print(obj.receiptID)
    #         print(obj.clientCode)
    #         print(obj.state)
    #         print(obj.expireDT)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
    
    # 출금동의 검증            
    # def test_verifyCMS(self) :
    #     try :
    #         obj = self.navercertService.verifyCMS(self.clientCode, '02310310230900000210000000000001')
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

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(NavercertServiceTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
