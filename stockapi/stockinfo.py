# -*- encoding: utf-8 -*-
"""
@File           : stockinfo.py
@Time           : 2020/3/12 19:51
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : stockapi
@description    : 描述
"""
import re
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from setting import *
from models import *
import aiohttp
from fastapi import FastAPI, Query, Body


app = FastAPI()

# 获取logger实例
logger = logging.getLogger(__name__)
# 指定输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s: %(message)s')

# 每天生成一个日志文件，保留最近30天的日志文件
log_file_name = __name__.split('.')[1]
timeRotateHandler = TimedRotatingFileHandler(filename=LOG_PATH.rstrip('/').rstrip('\\') + "/{}_".format(log_file_name),
                                             when="D", interval=1, backupCount=30, encoding='utf-8')
timeRotateHandler.setFormatter(formatter)
# timeRotateHandler.setLevel(logging.INFO)
# 删除日志文件设置
timeRotateHandler.suffix = '%Y-%m-%d_%H-%M.log'
timeRotateHandler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 为logger添加具体的日志处理器
logger.addHandler(timeRotateHandler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)


@app.post('/api/v1/stock/search', tags=['stock_v1'], summary='根据股票代码查询股票信息')
async def post_stockinfo_search(param: StocksModel = Body(..., example={
    "seq": "123",
    "bus": "100",
    "stocks": [
        "sz002885",
        "sh603863",
        "sz300675",
    ]
})):
    stock_list = []
    async with aiohttp.ClientSession() as session:
        stock_str = ",".join(param.stocks)
        url = STOCK_SINA_URL + stock_str
        async with session.get(url) as resp:
            # print(resp.status)
            res = await resp.text()
            # print(res, type(res))
            res_list = str(res).split(';')
            # print(len(res_list))
            for item in res_list[:-1]:
                # print(item)
                stock = item.split('=')[1]
                # print('股票：', stock)
                stock_details = stock.strip('"').split(',')
                stock_info = StockInfoModel()
                stock_info.name = stock_details[0]
                stock_info.today_start = stock_details[1]
                stock_info.yesterday_end = stock_details[2]
                stock_info.current_price = stock_details[3]
                stock_info.current_high = stock_details[4]
                stock_info.current_low = stock_details[5]
                stock_info.in_1_price = stock_details[6]
                stock_info.out_1_price = stock_details[7]
                stock_info.trade_quantity = stock_details[8]
                stock_info.trade_money = stock_details[9]
                stock_info.in_1_47_num = stock_details[10]
                stock_info.in_1_47_price = stock_details[11]
                stock_info.in_2_price = stock_details[12]
                stock_info.in_2_num = stock_details[13]
                stock_info.in_3_price = stock_details[14]
                stock_info.in_3_num = stock_details[15]
                stock_info.in_4_price = stock_details[16]
                stock_info.in_4_num = stock_details[17]
                stock_info.in_5_price = stock_details[18]
                stock_info.in_5_num = stock_details[19]
                stock_info.out_1_31_num = stock_details[20]
                stock_info.out_1_31_price = stock_details[21]
                stock_info.out_2_price = stock_details[22]
                stock_info.out_2_num = stock_details[23]
                stock_info.out_3_price = stock_details[24]
                stock_info.out_3_num = stock_details[25]
                stock_info.out_4_price = stock_details[26]
                stock_info.out_4_num = stock_details[27]
                stock_info.out_5_price = stock_details[28]
                stock_info.out_5_num = stock_details[29]
                stock_info.trade_date = stock_details[30]
                stock_info.trade_time = stock_details[31]

                stock_list.append(stock_info)

            return stock_list


"""
0：”大秦铁路”，股票名字；
1：”27.55″，今日开盘价；
2：”27.25″，昨日收盘价；
3：”26.91″，当前价格；
4：”27.55″，今日最高价；
5：”26.20″，今日最低价；
6：”26.91″，竞买价，即“买一”报价；
7：”26.92″，竞卖价，即“卖一”报价；
8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
10：”4695″，“买一”申请4695股，即47手；
11：”26.91″，“买一”报价；
12：”57590″，“买二”
13：”26.90″，“买二”
14：”14700″，“买三”
15：”26.89″，“买三”
16：”14300″，“买四”
17：”26.88″，“买四”
18：”15100″，“买五”
19：”26.87″，“买五”
20：”3100″，“卖一”申报3100股，即31手；
21：”26.92″，“卖一”报价
(22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
30：”2008-01-11″，日期；
31：”15:05:32″，时间；
"""


def main():
    logger.info('StockInfo API 运行中...')
    return app


if __name__ == '__main__':
    main()
