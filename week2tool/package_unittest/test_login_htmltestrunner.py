# 想生成的测试报告更详细，能在浏览器中打开
# 使用HTMLTestRunner模块生成测试报告
# 前置条件：直接现成的

"""
类：HMTLTestRunner(f,title,description)
    f:指文件对象，一般是HTML文件

"""

from project02.iter03_add_user import login
import unittest
import sys

from week2tool.package_unittest.HTMLTestRunner import HTMLTestRunner


class TestLogin(unittest.TestCase):

    # 1. 测试登录的测试用例

    # case1 : 输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('admin','123456').get('code')
        self.assertEqual(except_value,actual_value)

    # case2 : 输入错误的用户名或密码登录
    def test_user_wrong(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('bca', '123456').get('code')
        self.assertEqual(except_value, actual_value)

    # case3 : 输入空的用户或密码登录
    def test_password_is_null(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('admin', '').get('code')
        self.assertEqual(except_value, actual_value)


if __name__ == '__main__':

    # 创建一个条件a
    suite_a = unittest.TestSuite()
    suite_a.addTest(TestLogin('test_login_success'))
    suite_a.addTest(TestLogin('test_user_wrong'))
    suite_a.addTest(TestLogin('test_password_is_null'))
    print(suite_a)


    # 创建一个测试报告文件，HTML格式的
    test_report = './test_report.html'

    with open(test_report,'wb') as f:
        runner = HTMLTestRunner(f,title='测试报告',description='测试报告描述')
        runner.run(suite_a)
