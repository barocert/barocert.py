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
        self.kakocertService = KakaocertService('LINKHUB_BC', 'npCAl0sHPpJqlvMbrcBmNagrxkQ74w9Sl0A+M++kMCE=')
        self.kakocertService.IPRestrictOnOff = True
        self.kakocertService.UseLocalTimeYN = True
        self.clientCode = "023030000004"
        
    # def test_requestIdentity(self):
    #     identity = Identity(        
    #         receiverHP = self.kakocertService._encrypt('01054437896'),
    #         receiverName = self.kakocertService._encrypt('최상혁'),
    #         receiverBirthday = self.kakocertService._encrypt('19880301'),
    #         ci = '',
    #         reqTitle = '인증요청 메시지 제목란',
    #         expireIn = 1000,
    #         token = self.kakocertService._encrypt('본인인증요청토큰'),
    #         returnURL = 'https://kakao.barocert.com'
    #     )
        
    #     try :
    #         obj = self.kakocertService.requestIdentity(self.clientCode, identity)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # def test_getIdentityStatus(self) :
    #     try :
    #         obj = self.kakocertService.getIdentityStatus(self.clientCode, '02304190230300000040000000000039')
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
            
    # def test_verifyIdentity(self) :
    #     try :
    #         obj = self.kakocertService.verifyIdentity(self.clientCode, '02304190230300000040000000000039')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
    
    # def test_requestSign(self):
    #     sign = Sign(        
    #         receiverHP = self.kakocertService._encrypt('01054437896'),
    #         receiverName = self.kakocertService._encrypt('최상혁'),
    #         receiverBirthday = self.kakocertService._encrypt('19880301'),
    #         ci = '',
    #         reqTitle = '인증요청 메시지 제목란',
    #         expireIn = 1000,
    #         token = self.kakocertService._encrypt('전자서명단건테스트데이터'),
    #         tokenType = 'TEXT',
    #         appUseYN = False,
    #         returnURL = 'https://kakao.barocert.com'
    #     )
        
    #     try :
    #         obj = self.kakocertService.requestSign(self.clientCode, sign)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # def test_getSignState(self) :
    #     try :
    #         obj = self.kakocertService.getSignState(self.clientCode, '02304190230300000040000000000040')
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
            
    # def test_verifySign(self) :
    #     try :
    #         obj = self.kakocertService.verifySign(self.clientCode, '02304190230300000040000000000040')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # def test_requestMultiSign(self):
        
    #     multiSignTokens = []
    #     for x in range(0,5):
    #         multiSignTokens.append(
    #             MultiSignTokens(
    #                 reqTitle = "전자서명복수테스트",
    #                 token = self.kakocertService._encrypt("전자서명복수테스트데이터" + str(x)) 
    #             )
    #         )    
        
    #     multiSign = MultiSign(        
    #         receiverHP = self.kakocertService._encrypt('01054437896'),
    #         receiverName = self.kakocertService._encrypt('최상혁'),
    #         receiverBirthday = self.kakocertService._encrypt('19880301'),
    #         ci = '',
    #         reqTitle = '인증요청 메시지 제목란',
    #         expireIn = 1000,
    #         tokens = multiSignTokens,
    #         tokenType = 'TEXT',
    #         appUseYN = False,
    #         returnURL = 'https://kakao.barocert.com'
    #     )
        
    #     try :
    #         obj = self.kakocertService.requestMultiSign(self.clientCode, multiSign)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # def test_getMultiSignState(self) :
    #     try :
    #         obj = self.kakocertService.getMultiSignState(self.clientCode, '02304190230300000040000000000041')
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
            
    # def test_verifyMultiSign(self) :
    #     try :
    #         obj = self.kakocertService.verifyMultiSign(self.clientCode, '02304190230300000040000000000041')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         for multiSignedData in obj.multiSignedData:
    #             print(multiSignedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # def test_requestCMS(self):
    #     cms = CMS(        
    #         receiverHP = self.kakocertService._encrypt('01054437896'),
    #         receiverName = self.kakocertService._encrypt('최상혁'),
    #         receiverBirthday = self.kakocertService._encrypt('19880301'),
    #         ci = '',
    #         reqTitle = '인증요청 메시지 제목란',
    #         expireIn = 1000,
    #         requestCorp = self.kakocertService._encrypt("링크허브"),
    #         bankName = self.kakocertService._encrypt("국민은행"),
    #         bankAccountNum = self.kakocertService._encrypt("19-321442-1231"),
    #         bankAccountName = self.kakocertService._encrypt("최상혁"),
    #         bankAccountBirthday = self.kakocertService._encrypt("19880301"),
    #         bankServiceType = self.kakocertService._encrypt("CMS"),
    #         appUseYN = False,
    #         returnURL = 'https://kakao.barocert.com'
    #     )
        
    #     try :
    #         obj = self.kakocertService.requestCMS(self.clientCode, cms)
    #         print(obj.receiptID)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)
            
    # def test_getCMSStatus(self) :
    #     try :
    #         obj = self.kakocertService.getCMSStatus(self.clientCode, '02304190230300000040000000000042')
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
            
    # def test_verifyCMS(self) :
    #     try :
    #         obj = self.kakocertService.verifyCMS(self.clientCode, '02304190230300000040000000000042')
    #         print(obj.receiptID)
    #         print(obj.state)
    #         print(obj.signedData)
    #         print(obj.ci)
    #     except BarocertException as BE :
    #         print(BE.code)
    #         print(BE.message)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KakaocertServiceTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
