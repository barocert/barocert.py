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
from kakaocert import *

class KakaocertServiceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.kakocertService = KakaocertService('TESTER', 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I=')
        self.kakocertService.IPRestrictOnOff = True
        self.kakocertService.UseLocalTimeYN = True
        self.clientCode = "020040000001"

    def test_verifyCMS(self) :
        try :
            obj = self.kakocertService.verifyCMS(self.clientCode, "020050711485700002")
            print(obj)
        except BarocertException as KE :
            print(KE.code)
            print(KE.message)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KakaocertServiceTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
