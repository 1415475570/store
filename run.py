import unittest
from HTMLTestRunner import HTMLTestRunner
from day15.sendEmail import sendEmail
import time
# 创建测试集
suite = unittest.TestSuite()

# 使用测试加载器集中加载
loader =unittest.defaultTestLoader
tests = loader.discover("E:\\PyCharm\\A\\day15\\testcase",pattern="Test*.py")

suite.addTest(tests)

# 使用html运行器生成报告
f =  open("计算器测试报告.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="报告",
    verbosity=1,
    description="这是一个非常详细的测试报告"
)

runner.run(suite)
f.close()
# time.sleep(2)

# 加上email邮件发送
p=sendEmail()
p.send("1415475570@qq.com","1578133529@qq.com",'E:\\PyCharm\\A\\day15\\计算器测试报告.html')

# 定时发送
# def timer(n):
#     while True:
#         p.send("1415475570@qq.com", "1578133529@qq.com", 'E:\\PyCharm\\A\\day15\\计算器测试报告.html')
#         time.sleep(n)
# timer(5)