# 在此编写业务代码，例如先输入搜索内容，再点击搜索
# 本类仅供演示使用，不使用请注释掉本类
from page.handle.baiduHandle import baiduHandle


class baiduProxy:
    def __init__(self):
        self.baiduHandle = baiduHandle()

    def search(self,content):
        self.baiduHandle.input_search_content(content)
        self.baiduHandle.click_search_btn()
        return True