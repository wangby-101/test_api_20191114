# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 13:22
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : run.py
# @Software: PyCharm

import unittest
import HTMLTestRunnerNew
from Common import base_path

# 自动查找testcases目录下，以test开头的.py文件里面的测试类
discover = unittest.defaultTestLoader.discover(base_path.testcases_dir, pattern="test*.py", top_level_dir=None)
#
with open(base_path.reports_html, 'wb') as file:
    # 执行用例
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='API',
                                              description='API测试报告',
                                              tester='王柄印')
    runner.run(discover)  # 执行查找到的用例