from selenium import webdriver

import data

'''
@author lyingOn
@desc 获取浏览器驱动工具类
@date 2021-10-11
'''
class DriverUtil:
    _driver = None

    @staticmethod
    def noHead(options):
        # 无头模式
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')

    # 获取浏览器驱动对象，并完成初始操作
    # driverName 浏览器对象名称
    # isNoHead 是否启用无头模式
    @classmethod
    def get_driver(cls,driverName,isNoHead):
        # 如果为空则创建，不为空直接返回
        if cls._driver is None:
            if driverName == 'ie':
                cls.ie_options = webdriver.IeOptions()
                if isNoHead is True:
                    DriverUtil.noHead(cls.ie_options)
                cls._driver = webdriver.Ie(ie_options=cls.ie_options)
            elif driverName == 'chrome':
                cls.chrome_options = webdriver.ChromeOptions()
                if isNoHead is True:
                    DriverUtil.noHead(cls.chrome_options)
                cls._driver = webdriver.Chrome(chrome_options=cls.chrome_options)
            elif driverName == "firefox":
                cls.firefox_options = webdriver.FirefoxOptions()
                if isNoHead is True:
                    DriverUtil.noHead(cls.firefox_options)
                cls._driver = webdriver.Firefox(firefox_options=cls.firefox_options)
            else:
                raise Exception("This browser type is not supported,暂不支持此浏览器类型")
            cls._driver.maximize_window()
            # 设置隐式等待30秒
            cls._driver.implicitly_wait(30)
            cls._driver.get(data.global_url)
        return cls._driver

    # 关闭驱动对象
    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            # 清空对象
            cls._driver = None
