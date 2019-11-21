# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 13:44
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : test_recharge.py
# @Software: PyCharm
import json
import unittest
from ddt import ddt, data
from Common.do_excel import Do_Excel
from Common.base_path import data_file
from Common.log import MyLogger
from Common.request import Request
from Common.basic_data import Context

de = Do_Excel(data_file)
cases = de.get_case('recharge')
mylog = MyLogger()

@ddt
class TestRecharge(unittest.TestCase):

    def setUp(self):
        mylog.debug('开始测试')

    def tearDown(self):
        mylog.debug('清除数据')

    @data(*cases)
    def testrecharge(self, case):
        datas = json.loads(case.data)
        mylog.info("""================测试数据=================
                用例编号：{0}
                用例名称：{1}
                测试接口：{2}
                测试数据：{3}""".format(case.case_id, case.title, case.url, datas))
        cookies = getattr(Context, 'cookies')
        res = Request(method=case.method, url=case.url, data=datas, cookies=cookies)
        try:
            self.assertEqual(str(case.expected), res.get_json()['code'])
            mylog.info("用例{}执行通过".format(case.case_id))
            de.write_result(sheetname='recharge', case_id=case.case_id, actual=res.get_json()['code'], result='PASS')
        except AssertionError as e:
            mylog.info("用例{}执行失败".format(case.case_id))
            de.write_result(sheetname='recharge', case_id=case.case_id, actual=res.get_json()['code'], result='FALSE')
            raise e

if __name__ == '__main__':
    pass
