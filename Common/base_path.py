# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 13:40
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : base_path.py
# @Software: PyCharm

import os

basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例
data_dir = os.path.join(basepath, "Test_Data")
data_file = os.path.join(data_dir, "cases.xlsx")

# Conf
conf_dir = os.path.join(basepath, "Confs")

# Log
logs_dir = os.path.join(basepath, 'Logs')

# testcase
testcases_dir = os.path.join(basepath, 'Test_Cases')

# 测试报告
reports_dir = os.path.join(basepath, 'Reports')
reports_html = os.path.join(reports_dir, 'reports_html.html')
if __name__ == '__main__':
    print(data_file)