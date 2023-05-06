import time
from datetime import datetime
from zhdate import ZhDate

# 函数：简短日期
def getSimpleDate():
    # 获取当前日期时间，并格式化
    simple_date = time.strftime("%Y 年 %#m 月 %#d 日")
    return simple_date

# 函数：完整日期带时区（UTC+8）
def getFullDate():
    # 获取当前日期时间，并格式化
    full_date = time.strftime("%Y-%m-%d %H:%M:%S")
    return full_date

# 函数：中文化星期几
def getWeekday(full_date):
    # 获取星期几，中文化表示
    today = datetime.strptime(
        full_date, "%Y-%m-%d %H:%M:%S")  # 按指定格式转为 datetime 对象
    # 获取对应星期的索引值
    weekday_today = datetime.date(today).weekday()
    # 创建中文名称数组
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    # 返回中文化对应值
    weekday = weekdays[weekday_today]
    return weekday

# 函数：农历日期
def getZhDate():
    zhdate_today = ZhDate.today().chinese()[5:9]
    return zhdate_today


# 调用函数
if __name__ == "__main__":
    getSimpleDate()
    getFullDate()
    getWeekday(getFullDate())
    getZhDate()
