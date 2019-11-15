# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 14:09
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : Configs.py
# @Software: PyCharm

import os
import configparser
from Common.base_path import conf_dir

class Configs:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        switch = os.path.join(conf_dir, "switch.conf")
        self.conf.read(switch, encoding='utf-8')
        if self.getboolean("Switch", "on"):
            onlone = os.path.join(conf_dir, "onlone.conf")
            self.conf.read(onlone, encoding='utf-8')
        else:
            test = os.path.join(conf_dir, "test.conf")
            self.conf.read(test, encoding='utf-8')

    def get(self, section, option):
        return self.conf.get(section=section, option=option)

    def getint(self, section, option):
        return self.conf.getint(section=section, option=option)

    def getboolean(self, section, option):
        return self.conf.getboolean(section=section, option=option)

    def getfloat(self, section, option):
        return self.conf.getfloat(section=section, option=option)

if __name__ == '__main__':
    conf = Configs()
    print(conf.get("URL", "url"))