# 本类仅供演示使用，不使用请注释掉本类
import time
import unittest

from ddt import ddt, data, unpack

from data import testData
from page.proxy.baiduProxy import baiduProxy
from tools.DriverUtil import DriverUtil

@ddt()
class testBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver("chrome",True)
        cls.baiduProxy = baiduProxy()

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    #unpack为解包，当传入多个参数时需使用
    @data([testData.search_content_1], [testData.search_content_2])
    # @unpack
    def test_case_1(self,content):
        result = self.baiduProxy.search(content)
        time.sleep(3)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()