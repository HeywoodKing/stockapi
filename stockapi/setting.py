# -*- encoding: utf-8 -*-
"""
@File           : setting.py
@Time           : 2020/3/12 19:50
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : stockapi
@description    : 描述
"""
import os
import platform

STOCK_SINA_URL = 'http://hq.sinajs.cn/list='

LOG_PATH = os.path.dirname(os.getcwd()) + '/logs/'
if platform.system().lower() == 'windows':
    LOG_PATH = 'E:/logs/'
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)
elif platform.system().lower() == 'linux':
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)
else:
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)
