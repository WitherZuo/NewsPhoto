#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import datetime

from modules.zhdate import ZhDate

now_datetime = datetime.now()

# 根据操作系统决定日期格式
# Linux: https://stackoverflow.com/questions/9525944/python-datetime-formatting-without-zero-padding
DATE_FORMATS = {
    "linux": "%Y {Y} %-m {M} %-d {D}",
    "win32": "%Y {Y} %#m {M} %#d {D}",
    "darwin": "%Y {Y} %-m {M} %-d {D}",  # macOS
}


# 函数：获取当前时区
def get_timezone():
    print("- Getting the local timezone...")
    # 获取当前时区偏移量（单位：小时）
    utc_offset = now_datetime.astimezone().utcoffset()
    utc_offset_hours = utc_offset.total_seconds() / 3600  # 转换为小时
    timezone = f"UTC{'+' if utc_offset_hours >= 0 else ''}{int(utc_offset_hours)}"
    return timezone


# 函数：简短日期
def get_simple_date():
    print("- Getting the short time and date...")
    platform = sys.platform.lower()
    format_str = DATE_FORMATS.get(platform, "%Y {Y} %#m {M} %#d {D}")  # 默认格式
    simple_date = now_datetime.strftime(format_str).format(Y="年", M="月", D="日")
    return simple_date


# 函数：完整日期
def get_full_date():
    print("- Getting the full time and date...")
    # 获取当前日期时间，并格式化
    full_date = now_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return full_date


# 函数：中文化星期几
def get_weekday(full_date):
    print("- Getting the weekday...")
    # 获取星期几，中文化表示
    today = datetime.strptime(
        full_date, "%Y-%m-%d %H:%M:%S"
    )  # 按指定格式转为 datetime 对象
    weekday_index = today.weekday()  # 获取对应星期的索引值
    weekdays = (
        "星期一",
        "星期二",
        "星期三",
        "星期四",
        "星期五",
        "星期六",
        "星期日",
    )
    weekday = weekdays[weekday_index]
    return weekday


# 函数：农历日期
def get_zh_date():
    print("- Getting Chinese date...")
    try:
        # 获取农历日期
        zhdate_full = ZhDate.today().chinese()
        if "闰" in zhdate_full:
            zhdate_today = zhdate_full[5:10]
        else:
            zhdate_today = zhdate_full[5:9]
        return zhdate_today
    except Exception as e:
        print(f"Error fetching Chinese date: {e}")
        return "Failed to fetch Chinese date."
