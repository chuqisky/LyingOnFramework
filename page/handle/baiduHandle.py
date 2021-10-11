# 在此编写操作代码，例如文本框输入，点击等
# 本类仅供演示使用，不使用请注释掉本类
from LyingOn.BaseHandle import BaseHandle

from page.element.baiduElement import baiduElement


class baiduHandle(BaseHandle):
    def __init__(self):
        self.baiduElement = baiduElement()

    def input_search_content(self,content):
        try:
            self.base_input(self.baiduElement.find_search_input(),content)
        except:
            pass

    def click_search_btn(self):
        try:
            self.base_click(self.baiduElement.find_search_btn())
        except:
            pass