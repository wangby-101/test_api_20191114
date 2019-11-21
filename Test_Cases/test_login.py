# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 10:55
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : test_login.py
# @Software: PyCharm
import json
import unittest
from ddt import ddt, data
from Common.base_path import data_file
from Common.do_excel import Do_Excel
from Common.log import MyLogger
from Common.request import Request

de = Do_Excel(data_file)
cases = de.get_case('login')
myloger = MyLogger()
COOKIES = None
@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        myloger.debug('开启执行测试')
    def tearDown(self):
        myloger.debug('结束测试')
    @data(*cases)
    def testlogin(self, case):
        datas = json.loads(case.data)
        myloger.info("""================测试数据=================
        用例编号：{0}
        用例名称：{1}
        测试接口：{2}
        测试数据：{3}""".format(case.case_id, case.title, case.url, datas))
        res = Request(method=case.method, url=case.url, data=datas)
        # if res.get_cookies():
        #     global COOKIES
        #     COOKIES = res.get_cookies()
        try:
            self.assertEqual(case.expected, res.get_text())
            de.write_result('login', case_id=case.case_id, actual=res.get_text(), result='Pass')
        except AssertionError as e:
            myloger.info('用例执{}行失败'.format(case.case_id))
            de.write_result('login', case_id=case.case_id, actual=res.get_text(), result='False')
            raise e
