# -*- coding: utf-8 -*-
"""
# Copyright (c) 2019 LinkDoc, Inc. All Rights Reserved
# @file    : calcu_work_days.py
# @date    : 2019/9/19 5:32 下午
# @author  : kaijiang@linkdoc.com
# @brief   : 
"""

import pandas as pd
import re

date_series = pd.date_range('2019-10-21', '2019-11-29', freq=pd.tseries.offsets.BDay())
date_str = str(date_series)

pattern = re.compile(r"(\d{4}-\d{1,2}-\d{1,2})")   # 查找日期
date_list = pattern.findall(date_str)

print(','.join([x.replace('2019-', '') for x in date_list]))
