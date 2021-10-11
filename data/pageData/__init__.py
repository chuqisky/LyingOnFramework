# 存放page包中使用到的变量
# 分级方式为_init_.py存放page全局变量，对于单个文件内的局部变量再新建文件夹存放
# 例如：
# _init_.py
#     page1(package)  _init_.py
#     page2(package)  _init_.py
from selenium.webdriver.common.by import By

search_text = (By.ID,'kw')
search_btn = (By.ID,'su')