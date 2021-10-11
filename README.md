 # 使用本框架前请先安装lyingOn
 pip install lyingOn
 pip install --upgrade lyingOn
 
 # 本框架推荐使用BeautifulReport生成自动化测试报告，若想使用HTMLTestRunner请自行切换
 将项目中的BeautifulReport文件夹放至本地python的/Lib/site-packages/目录下，放置完成后可删除本项目的BeautifulReport文件夹
 
 # 框架架构
 框架秉承高内聚低耦合概念，为便于管理，采用分层思想，所有测试操作均分为三层
 元素层(element)-操作层(handle)-业务层(proxy)
 元素层：用于查找元素，继承lyingOn中的basepage，主要编写元素查找方法
 操作层：操作元素，执行某个操作，例如点击，继承lyingOn中的basehandle，主要编写单个操作方法，依赖于元素层
 业务层：整合操作完成业务，将多个操作合并从而完成一个业务流程，例如将输入搜索内容与点击搜索合并完成业务搜索，主要编写单个业务方法，依赖于操作层
 
 script中的测试用例再对业务层进行调用，组合业务操作从而完成一个测试用例
 
 # 框架结构介绍
 base：存放项目中重复性出现的方法
 data：
    --pageData：存放page包中需使用到的变量
    --testData：存放script包中需使用到的变量
 log：存放日志文件
 page：
    --element：查找元素py文件
    --handle：操作元素py文件
    --proxy：业务py文件
 report：存放测试报告
 screenshot：存放截图
 script：测试脚本，测试用例存放处
 tools：存放项目使用到的一些工具
 config.py：项目配置文件
 run_suite.py：项目总启动文件，批量启动测试脚本
 
# 作者从事java开发，若有测试设计封装不到位之处，框架年久失修等问题，请向作者反馈
# 邮箱：chuqisky@gmail.com