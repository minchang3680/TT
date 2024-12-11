# import calendar
# calendar.prcal(2024)
# calendar.prmonth(2024,6)
# print(calendar.weekday(2024,12,25))

import datetime
import calendar

days = ['월','화','수','목','금','토','일']

weekday = datetime.date.today().weekday()
print(weekday)
print('오늘은' + days[weekday]+ '요일')

weekday = datetime.date(2024,12,25).weekday()
print(weekday)
print('크리스마스는 ' + days[weekday] + '요일')

# # 날짜로 요일 알아내기 - 함수로 정의
# def get_weekday(yyyy,mm,dd):
#     days = ['월','화','수','목','금','토','일']
#     weekday = datetime.date(yyyy,mm,dd).weekday()
#     print(f"{yyyy}년 {mm}월 {dd}일 {days[weekday]}요일")

# get_weekday(2024,12,25)

# import time

# print(time.time())
# time.sleep(2)
# print(time.sleep(2))

# a = time.time()
# time.sleep(2)
# b = time.time()
# # print(b-a)

# print(time.localtime())
# time_str = time.localtime()
# print(time_str.tm_year)

# print(time.ctime())  # 시간을 스트링 형태로 표기해준다.
# print(time.ctime(a))
# print(time.ctime(b))

# # 1970년 1월 1일 기준.
# year = time.time()/(365*24*60*60)  # 특정 기준으로부터 몇년이 지났는가.
# print(year)
# day = time.time()/24*60*60  # 특정 기준으로부터 몇 일이 지났는가
# print(day)

# import time

# def check_time(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print("수행시간 : " + str(end - start) + "초")

# def a():
#     for i in range(10):
#         print(i)
#         time.sleep(1)

# def b():
#     for i in range(100):
#         print(i)
#         time.sleep(0.5)

# # check_time(a)
# check_time(b)

