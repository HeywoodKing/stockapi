# -*- encoding: utf-8 -*-
"""
@File           : run.py
@Time           : 2019/12/2 20:13
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : moli_restapi
@description    : 描述
"""
import os
import sys
import time
# import subprocess
from config import *
from threading import Thread
from multiprocessing import Process
# from concurrent.futures.thread import ThreadPoolExecutor
# from concurrent.futures.process import ProcessPoolExecutor

"""
daphne
stockinfo:
daphne -b 192.168.1.79 -p 38080 run:app
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

pwd = os.getcwd()


# api 启动统一入口
def start_api(item):
    """
    api 启动统一入口
    :param item:
    :return:
    """
    try:
        # a = os.system(command="{}".format(pwd[0:pwd.index('\\')]))
        # b = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        # b = os.system(cmd)

        cmd = r"{}\{}".format(pwd, item['name'])
        os.chdir(cmd)

        print('\r\n')
        print('+' * 100)
        print('{}>>{}:{} api 服务正在启动...'.format(item['name'], item['host'], item['port']))
        print('+' * 100)

        # uvicorn
        # args = """{} {}:{} --host {} --port {} --limit-concurrency 100 --loop asyncio
        # --timeout-keep-alive 5 """.format(item['wsgi'], item['module'], item['app'], item['host'], item['port'])

        # daphne
        args = "{} -b {} -p {} {}:{}".format(item['wsgi'], item['host'], item['port'], item['module'], item['app'])

        # gunicorn
        # args = "{} --workers=4 --bind={}:{} {}:{}".format(item['wsgi'], item['host'], item['port'], item['module'], item['app'])

        res = os.system(command=args)

        # res = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE)
        # print(item['name'], res, res >> 8)
        # if res:
        #     # os.system(command="python demo.py")
        #     print('{}>>{}:{} api 服务启动成功，正在运行中...'.format(item['name'], item['host'], item['port']))
        # else:
        #     print('factory 切换路径错误！')

    except Exception as ex:
        print('{}>>{}:{} api 服务启动异常，{}'.format(item['name'], item['host'], item['port'], ex))


def main():
    # print('当前路径 {}'.format(pwd))
    # sub = subprocess.Popen("pipenv shell", shell=True, stdout=subprocess.PIPE)
    # sub.wait()
    # print(sub.read())

    # os.system('pipenv shell')
    # os.system('dir')

    # t1 = Thread(target=start_factory)
    # t1.start()
    # t2 = Thread(target=start_words)
    # t2.start()

    # p1 = Process(target=start_factory)
    # p1.start()
    # p2 = Process(target=start_words)
    # p2.start()

    for item in API_LIST:
        if IS_THREAD_RUN_METHOD:
            t = Thread(target=start_api, args=(item,))
            t.start()

        else:
            p = Process(target=start_api, args=(item,))
            p.start()

        time.sleep(1)


if __name__ == '__main__':
    main()
