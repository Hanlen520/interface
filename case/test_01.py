import unittest
from eyebows_interface.common.logger import Log


class DemoTest(unittest.TestCase):
    log = Log()
    def test_one(self):
        self.log.info("start----开始执行第一条case")
        self.assertTrue(True)
        print('start-----第一条case')
    def test_two(self):
        self.log.info("start----开始执行第二条case")
        self.assertTrue(False)
        print('start-----第二条case')