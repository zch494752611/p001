from project02.iter03_add_user import login     # 导入项目
from loguru import logger

import unittest

import sys

class TestLogin(unittest.TestCase):

    # 初始化类方法
    @classmethod
    def setUpClass(cls) -> None:
        print("开始运行方法：", sys._getframe().f_code.co_name)

    # 清空类方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("开始运行方法：", sys._getframe().f_code.co_name)

    # 初始化方法
    def setUp(self) -> None:
        print("开始运行方法：", sys._getframe().f_code.co_name)

    # 清除方法
    def tearDown(self) -> None:
        print("开始运行方法：", sys._getframe().f_code.co_name)

    # 1.测试登陆的测试用例

    # case1 : 输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        except_value = 0
        actual_value = login('admin', '123456').get('code')
        self.assertEqual(except_value, actual_value)

# case2 ： 输入错误的用户名或密码登录
    def test_user_wrong(self):
        except_value = 1
        actual_value = login('bca', '123456').get('code')
        self.assertEqual(except_value, actual_value)

# case3 ： 输入空的用户名和密码登录
    def test_password_is_null(self):
        except_value = 1
        actual_value = login('admin','').get('code')
        self.assertEqual(except_value,actual_value)

if __name__ == '__main__':
    unittest.main()



# 2.进行测试 - 使用断言 ： assert 值1 操作符 值2
# 测试方法 ： 预期结果 和 实际结果 进行比较

# 以上用例 登陆成功的预期结果是code = 0

# login_result = login('admin','123456')
# logger.debug("登录返回数据：{}".format(login_result))
#
# assert 0 == login("admin","123456").get('code')


# 存在的问题:
"""
1.无法查看运行的用例数，比如成功了几条，失败了几条
2.如果失败了，是因为什么导致的？最好给出失败的错误日志
3.无法去组织用例，不能控制哪些用例执行，哪些不执行
"""

