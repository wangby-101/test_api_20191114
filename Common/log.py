# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 9:51
# @Author  : Wang Bingyin
# @Email   : xxxxxxx@163.com
# @File    : log.py
# @Software: PyCharm
import os
import time
import logging
import HTMLTestRunnerNew
from Common.base_path import logs_dir

logger = logging.getLogger('wangbingyin')
logger.setLevel('DEBUG')

def get_log_dir():
    log_dir = os.path.join(logs_dir, get_current_day())
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    else:
        return log_dir

def get_current_day():
    return time.strftime('%Y%m%d', time.localtime(time.time()))

def add_handler(level):
    if level == 'ERROR':
        logger.addHandler(MyLogger.error_handler)
    else:
        logger.addHandler(MyLogger.info_handler)
    logger.addHandler(MyLogger.ch)
    logger.addHandler(MyLogger.report_handler)

def remove_handler(level):
    if level == 'ERROR':
        logger.removeHandler(MyLogger.error_handler)
    else:
        logger.removeHandler(MyLogger.info_handler)
    logger.removeHandler(MyLogger.ch)
    logger.removeHandler(MyLogger.report_handler)

class MyLogger:
    print(get_log_dir())
    log_dir = get_log_dir()
    error_file = os.path.join(log_dir, 'error.log')
    info_file = os.path.join(log_dir, 'info.log')
    formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    error_handler = logging.FileHandler(filename=error_file, encoding='utf-8')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    info_handler = logging.FileHandler(filename=info_file, encoding='utf-8')
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    report_handler = logging.StreamHandler(HTMLTestRunnerNew.stdout_redirector)
    report_handler.setLevel(logging.DEBUG)
    report_handler.setFormatter(formatter)

    @staticmethod
    def debug(msg):
        add_handler('EBUG')
        logger.debug(msg)
        remove_handler('DEBUG')

    @staticmethod
    def info(msg):
        add_handler('INFO')
        logger.info(msg)
        remove_handler('INFO')

    @staticmethod
    def warning(msg):
        add_handler('WARNING')
        logger.warning(msg)
        remove_handler('WARNING')

    @staticmethod
    def error(msg):
        add_handler('ERROR')
        logger.error(msg)
        remove_handler('ERROR')

    @staticmethod
    def critical(msg):
        add_handler('CRITICAL')
        logger.critical(msg)
        remove_handler('CRITICAL')


if __name__ == '__main__':
    mylog = MyLogger()
    mylog.debug('=====DEBUG=====')
    mylog.info('=====INFO=====')
    mylog.warning('=====WARNING=====')
    mylog.error('=====ERROR=====')
    mylog.critical('=====CRITICAL=====')