# -*- encoding: utf-8 -*-
"""
@File           : models.py
@Time           : 2020/3/12 20:07
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : stockapi
@description    : 描述
"""
import time
import random
from typing import List
from pydantic import BaseModel, Field


class EntityModel(BaseModel):
    seq: str = Field(default=time.time() + random.randint(1000, 9999), title='本次作业序列号', )
    bus: str = Field(default=time.time() + random.randint(1000, 9999), title='本次作业业务号', )
    # pass


class StocksModel(EntityModel):
    stocks: List[str] = Field(default='', title='股票代码列表')


class StockInfoModel(BaseModel):
    stock_no: str = Field(default='', title='股票代码')
    name: str = Field(default='', title='股票名称')
    today_start: float = Field(default=0.00, title='今日开盘价')
    yesterday_end: float = Field(default=0.00, title='昨日收盘价')
    current_price: float = Field(default=0.00, title='当前价格')
    current_high: float = Field(default=0.00, title='今日最高价')
    current_low: float = Field(default=0.00, title='今日最低价')
    in_1_price: float = Field(default=0.00, title='竞买价，即买一报价')
    out_1_price: float = Field(default=0.00, title='竞卖价，即卖一报价')
    trade_quantity: float = Field(default=0.00, title='成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百')
    trade_money: float = Field(default=0.00, title='成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万')
    in_1_47_num: float = Field(default=0.00, title='买一申请4695股，即47手')
    in_1_47_price: float = Field(default=0.00, title='买一报价')
    in_2_price: float = Field(default=0.00, title='买二')
    in_2_num: float = Field(default=0.00, title='买二')
    in_3_price: float = Field(default=0.00, title='买三')
    in_3_num: float = Field(default=0.00, title='买三')
    in_4_price: float = Field(default=0.00, title='买四')
    in_4_num: float = Field(default=0.00, title='买四')
    in_5_price: float = Field(default=0.00, title='买五')
    in_5_num: float = Field(default=0.00, title='买五')
    out_1_31_num: float = Field(default=0.00, title='卖一申报3100股，即31手')
    out_1_31_price: float = Field(default=0.00, title='卖一报价')
    out_2_price: float = Field(default=0.00, title='卖二')
    out_2_num: float = Field(default=0.00, title='卖二')
    out_3_price: float = Field(default=0.00, title='卖三')
    out_3_num: float = Field(default=0.00, title='卖三')
    out_4_price: float = Field(default=0.00, title='卖四')
    out_4_num: float = Field(default=0.00, title='卖四')
    out_5_price: float = Field(default=0.00, title='卖五')
    out_5_num: float = Field(default=0.00, title='卖五')
    trade_date: str = Field(default='', title='交易日期')
    trade_time: str = Field(default='', title='交易时间')

