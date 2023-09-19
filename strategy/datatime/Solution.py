import typing
import datetime

original_string = "2023-09-15 12:00:00"
# 将字符串转换为 datetime 对象
original_datetime = datetime.datetime.strptime(original_string, "%Y-%m-%d %H:%M:%S")
# 要添加的微秒数
current_datetime = datetime.datetime.now()
current_microseconds_to_add = current_datetime.microsecond  # 500,000 微秒 = 0.5 秒
print("当前时间的微妙值：", current_microseconds_to_add)
# 创建一个 timedelta 对象来表示要添加的微秒
microseconds_delta = datetime.timedelta(microseconds=current_microseconds_to_add)

# 添加微秒
new_datetime = original_datetime + microseconds_delta

# 将新的 datetime 对象格式化为字符串
new_string = new_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")

print("原始字符串:", original_string)
print("添加微秒后的字符串:", new_string)


def get_date_by_str(time_str: typing.Union[str, datetime.datetime]):
    if not isinstance(time_str, str):
        return time_str
    if is_valid_date(time_str):
        """将当前时间的微秒值拼接加给time_str"""
        now = datetime.datetime.now()
        now_microseconds = now.microsecond
        timedelta = datetime.timedelta(microseconds=now_microseconds)
        time_obj = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        time_with_microseconds = time_obj + timedelta
        return time_with_microseconds
    return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")


def is_valid_date(str_date):
    """判断是否是一个有效的日期字符串"""
    try:
        datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
        return True
    except:
        return False


print(get_date_by_str(original_string))
