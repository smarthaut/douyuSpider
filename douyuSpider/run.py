#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 13:31
# @Author  : huanghe
# @Site    : 
# @File    : run.py
# @Software: PyCharm
from scrapy import cmdline

cmdline.execute('scrapy crawl douyu'.split())