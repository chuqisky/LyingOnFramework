import os
import unittest

from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    # BeautifulReport使用
    test_path = os.path.join(os.getcwd(),'script')
    discover = unittest.defaultTestLoader.discover(test_path,'test*.py',top_level_dir=None)
    BeautifulReport(discover).report(description='测试百度搜索', filename="百度自动化测试报告", log_path=os.path.join(os.getcwd(),'report'))

    # pass
