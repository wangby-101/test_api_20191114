# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 14:05
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : basic_data.py
# @Software: PyCharm

from Common.Configs import Configs

class Context:
    config = Configs()
    # 投资人测试数据
    # normal_user = config.get('basic', 'normal_user')
    # normal_pwd = config.get('basic', 'normal_pwd')
    # normal_member_id = config.get('basic', 'normal_member_id')
    # 管理员测试数据
    # admin_user = config.get('basic', 'admin_user')
    # admin_pwd = config.get('basic', 'admin_pwd')
    # # 借款人测试数据
    # loan_member_id = config.get('basic', 'loan_member_id')

if __name__ == '__main__':
    setattr(Context, 'cookies', "123456")
    print(getattr(Context, 'cookies'))