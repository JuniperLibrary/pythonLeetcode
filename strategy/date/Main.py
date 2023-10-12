import datetime

"""
datetime是datetime模块中的一个类，用于表示特定的时间点，包括日期和时间信息（年、月、日、小时、分钟、秒、微秒）。
datetime.datetime的实例具有诸如year、month、day、hour、minute、second和microsecond等属性。
"""
dt = datetime.datetime(2023, 9, 27, 14, 30)  # 2023-09-27 14:30:00
print(dt)
"""
date也是datetime模块中的一个类，用于表示日期（年、月、日），不包括时间组件。
datetime.date的实例具有诸如year、month和day等属性。
"""
d = datetime.date(2023, 9, 27)  # 表示2023年9月27日
print(d)
