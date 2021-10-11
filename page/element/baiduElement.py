# 在此编写查找元素代码
# 本类仅供演示使用，不使用请注释掉本类
from LyingOn.BasePage import BasePage

from data import pageData
from tools.DriverUtil import DriverUtil


class baiduElement(BasePage):
    def __init__(self):
        super().__init__()
        self.driver = DriverUtil.get_driver("chrome",True)

    # 获取搜索框
    def find_search_input(self):
        return self.base_find_elt(self.driver,pageData.search_text)

    # 获取搜索按钮
    def find_search_btn(self):
        return self.base_find_elt(self.driver,pageData.search_btn)