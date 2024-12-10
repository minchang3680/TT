# #실습2) Supermarket 클래스
# class Supermarket:
#     count = 0
#     def __init__(self,location,name,product,customer):
#         Supermarket.count += 1
#         self.location = location
#         self.name = name
#         self.product = product
#         self.customer = customer


#     def print_loction(self):
#         print(f"location : {self.location}")

#     def change_category(self,product):
#         self.product = product
    
#     def show_list(self):
#         print(self.product)

#     def enter_customer(self):
#         self.customer += 1

#     def show_info(self):
#         print(f"name : {self.name}, location : {self.location}, product : {self.product}, customer : {self.customer}")

#     def show_supermaket_count(self):
#         print(f"supermaket count: {Supermarket.count}")

# a = Supermarket("응암","이마트","프라이팬",4)
# a.print_loction()
# a.change_category("과자")
# a.show_list()
# a.enter_customer()
# a.show_info()
# a.show_supermaket_count

# class Country:
#     def __init__(self):
#         self.name = "나라이름"
#         self.population = "인구"
#         self.capital = "수도"
    
#     def show(self):
#         print('국가 클래스의 메소드입니다')

# class Korea(Country):
#     def __init__(self,name):
#         self.name = name
    
#     def show_name(self):
#         print('국가 이름은 :' ,self.name)

# country = Korea("대한민국")
# country.show()
# print(country.name)
# country.show_name()

# # 실습3)
# # 다음과 같은 조건을 만족하는 MinLimintcalculator 클래스 만들기
# # 1) Calcuator 클래스를 상속 받는다.
# # 2) value 값이 음수가 안되게 제한한다.
# # 3) sub() 메서드를 오버라이딩 하여 2번 조건을 만족시킬 것

# class Calcuator():
#     def __init__(self):
#         self.value = 100

#     def sub(self, value):
#         self.value -= value

# class MinLimintcalculator(Calcuator):

#     def sub(self, value):
#         self.value = max(0,self.value-value)
#         # super().sub(value)
#         # self.value = max(0,self.value)

# cal = MinLimintcalculator()
# cal.sub(20)
# cal.sub(90)
# print(cal.value)

# import calc_module # ctrl + 클릭 하면, 동일한 명의 파일로 이동이 가능하다.

# print(calc_module.add(1,2))
# print(calc_module.sub(1,2))
# print(calc_module.mul(1,2))
# print(calc_module.div(1,2))

# from calc_module import add

# print(add(1,2)) # 다른 것 없이 add만 가져옴.
# # calc_module.add() # 안됨

# import calc_module as cm

# print(cm.add(1,2)) # 모듈 명을 변경하고 함수 사용.

# import math
# print(math.floor(3.141592))
# print(math.ceil(3.141592))
# print(math.sqrt(9))

# from math import floor,ceil
# print(floor(3.141592))
# print(ceil(3.141592))

# import random

# print(random.randint(1,5))
# print(random.uniform(1,2))
# print(random.random())
# print(random.randrange(1,5,2))
# print(random.randrange(1,3))

# #up and down 게임 (숫자를 추츨해서 맞히는 게임)

# import random

# com = random.randint(1,100)

# min_v = 1
# max_v = 100
# count = 0
# score = 100

# while True:
#     try:
#         guess = int(input("숫자 입력(%d ~ %d) : " % (min_v, max_v)))
#         guess
#         if guess < 0 or guess > 100:
#             print("입력 범위를 초과했어요")
#         elif com == guess:
#             print("정답이예요!!")
#             print(f"{count}회 - {score}점입니다.")
#             break
#         elif com > guess:
#             print("램덤 수 보다 작아요")
#             min_v = guess
#             score -= 10
#             count += 1
#         else:
#             print("랜덤 수 보다 커요")
#             max_v = guess
#             score -= 10
#             count += 1
#         if score == 10:
#             print(f"{count}회 - 0점입니다.")
#             break

#     except ValueError:
#         print("숫자만 입력 가능합니다.")

# # 실습. 로또 번호 뽑기
# # 1~45까지의 수 중 랜덤으로 6개의 숫자를 뽑는다 .
# # 6개의 숫자 중 중복되는 숫자가 없도록 한다.

# import random

# com = []  # 선택된 숫자들을 저장할 리스트

# # 6개의 고유한 숫자를 선택할 때까지 반복
# while len(com) < 6:
#     num = random.randint(1, 45)  # 1부터 45까지의 랜덤 숫자 생성
#     if num not in com:  # 숫자가 이미 선택된 숫자 리스트에 없으면
#         com.append(num)  # 리스트에 추가
        

# 6개의 고유한 숫자 출력
# print(com)

# import datetime

# now = datetime.datetime.today()
# print(now)
# print(now.year)

# print(f"{now.hour}시 {now.minute}분 {now.second}초")

# 나이가 100세 되는 해의 연도 계산하기 프로그램.

import datetime

today = datetime.date.today()
print(today.year)


# 지나온 날짜 계산하기

print("지금까지 몇일?")
first_day = datetime.date(2024,11,25)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time)
print(f'개강 이후 {passed_time.days}일 지났습니다.')