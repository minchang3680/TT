# d = [
#     [3, 1],
#     [3, 2],
#     [3, 3],
#     [3, 4],
#     [3, 5],
#     [3, 6],
#     [3, 7],
#     [3, 8],
#     [3, 9],
# ]
# # for x, y in d:
# #     print(f"{x} x {y} = {x*y}")


# for i in d:
#     print(f"{i[0]} x {i[1]} = {i[0]*i[1]}")

# 함수 시작

# 내장 함수
# a = "Strawberry Moon"
# print(len(a)) 
# print(a.count("r"))

# #함수의 기본적인 사용법
# def 함수 이름 (매개변수1,매개변수2 ...):
#     수행문 1
#     수행문 2
#     return 반환값

# def print_gugudan(dan):
#     for i in range(1,10):
#         print(dan,'x',i,'=',(dan*i))
# print_gugudan(5)

# def f(x):
#     result = x**2 + x*2 + 1
#     return result
# print(f(3))

# def sayHi():
#     print("Hi")
#     print("Hi")
#     print("Hi")

# sayHi()

# def sum_n(n):
#     sum_v = 0
#     for i in range(1,n+1):
#         sum_v += i
#     return sum_v
# print(sum_n(10))

# 함수 호출
# 함수명()

# x =10

# def func2():
#     print("func2",x)
# func2()

# def func():
#     x = 20
#     y = 11
#     print("func",x,y)
# func()
# print("main",x)
# # print("main",y) # y는 함수 내부에 있던 것이고 메인에는 없던 변수이기 떄문에 에러가 난다.

# def func3(x):
#     print("func3",x)

# func3(3)

# 실습1) 두수(2,2)를 매개 변수 전달하여 서로 같으면 곱하고 , 
# 서로 다르면 더하는 함수를 정의 하고 호출하는 프로그램을 작성하세요.

# def fun(x, y):
#     if x == y:
#         print("곱한 경우 : ",x*y)
#     else:
#         print("더한 경우 : ",x+y)
# fun(2,2)
# fun(2,3)  # print(fun(2,3)) 결과 출력은 되지만, print할게 없어서 None가 같이 출력된다
# return이 뭔지 아직 잘 모르겠네..

#실습2) 주문 상품 가격이 20,000원 미만이면 배송비(2500)원 포함하고, 
# 아니면 배송비를 포함하지 않는 프로그램을 작성하세요.

# def fu(x,y):
#     if x*y < 20000:
#         print("20,000원 미만의 경우 배송비가 붙습니다.",f"{x*y}원 일떄, 총 가격은 : {x*y+2500}")   
#         return
#     else:
#         print("20,000원 이상의 경우 배송비가 부과되지 않습니다",f"{x*y}원 일떄, 총 가격은 : {x*y}")
#         return
      
# fu(30000,1)
# fu(17500,1)

# def times(a):
#     a2 = [i*3 for i in a]
#     return a2
# v = [1,2,3,4,5]
# v2 = times(v)
# print(v2)
# print(type(v2))


# def times(l):
#     l2 = [i*2 for i in l]
#     return set(l2)
# v2 = times([1,2,3,4,5])
# print(v2)

# def sum_mul(a,b):
#     sum = a+b
#     mul = a*b
#     return sum, mul
# s, m = sum_mul(2,3)
# print(s, m)

# 실습3) 자판기 프로그램 함수화
# 저번 시간에 한 자판기 프로그램을 함수화 해보세요.
# 1. check_machine : 남은 음료수를 확인 할 수 있는 함수
# 2. is_drink : 음료수가 있는지 확인하는 함수
# 3. add_drink : 음료수를 추가하는 함수
# 4. remove_drink : 음료수를 제거하는 함수.

# vending_machne = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']
# user = input('소비자와 주인 가운데 입력하세요 :')

# if user=="소비자":
#     음료 = input("마시고 싶은 음료? :")
#     if 음료 in vending_machne:
#         print(f"{음료}드릴게요.")
#         vending_machne.remove(음료)
#     elif 음료 not in vending_machne :
#         print(f"{음료}는 없는 음료입니다.")
    

# elif user =="주인":
#     추가삭제 = input('추가 혹은 삭제 가운데 선택하여주세요.')    
#     if 추가삭제 == "추가":
#         추가음료=input("추가할 음료를 입력하여주세요.:")
#         index=vending_machne.index(추가음료)  #해당 동일한 추가음료의 위치를 찾는다.
#         vending_machne.insert(index,추가음료)  #찾은 위치에 동일 해당음료를 넣는다.
#     else:
#         추가삭제 == "삭제"
#         삭제음료 = input("삭제할 음료를 입력하여주세요.:")
#         if 삭제음료 in vending_machne:
#             vending_machne.remove(삭제음료)
#         else: print(f"{삭제음료}는 현재 없습니다.")
# print(vending_machne)
# vending_machne = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']

# 1. check_machine : 남은 음료수를 확인 할 수 있는 함수
# def check_machine():
#     print("남은 음료수 :",vending_machne)
# check_machine()
# # 2. is_drink : 음료수가 있는지 확인하는 함수
# def is_drink(a):
#     if a in vending_machne:
#         print(f"{a}가 있습니다.")
#     else: print(f"{a}가 없습니다.")
# is_drink("포카리")
# is_drink("게토레이")
# # 3. add_drink : 음료수를 추가하는 함수
# def add_drkink(b):
#     vending_machne.append(b)
#     vending_machne.sort
# add_drkink("포카리")
# print("추가된 음료 :",vending_machne)
# # 4. remove_drink : 음료수를 제거하는 함수.
# def remove_drink(c):
#     vending_machne.remove(c) 
# remove_drink("생수")
# print("제거된 음료 :",vending_machne)

# 실습4) 함수&스택
# 정수를 저장하는 스택을 구현한 다음 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 총 5가지 명령어이다.
# push x = 정수 x를 스택에 넣는 연산이다.
# pop = 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 있는 정수가 없는 경우 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다. 

# import sys
# n = int(sys.stdin.readline())

# stack=[]

# def push(num):
#     stack.append(num)

# def pop():
#     if len(stack)==0:
#         print(-1)
#     else:
#         print(stack.pop())

# def size():
#     print(len(stack))

# def empty():
#     if len(stack)==0:
#         print(1)
#     else:
#         print(0)

# def top():
#     if len(stack)==0:
#         print(-1)
#     else:
#         print(stack[-1])

# for _ in range(n):
#     command = sys.stdin.readline().split()
#     cmd = command[0]

#     if cmd == 'push':
#         push(command[1])
#     elif cmd == 'pop':
#         pop()
#     elif cmd == 'size':
#         size()
#     elif cmd == 'empty':
#         empty()
#     elif cmd == 'top':
#         top()

    # match cmd:
    #     case 'push':
    #         push(command[1])
    #     case 'pop':
    #         pop()
    #     case 'size':
    #         size()
    #     case 'empty':
    #         empty()
    #     case 'top':
    #         top()

# def oneUP():
#     global x
#     x += 1
#     return x

# x = 0
# print(oneUP())
# print(oneUP())
# print(oneUP())

#실습5) 1~30까지의 자연수 중 배수와 배수의 개수를 계산하는 함수를 정의 하시오.

# def get_times(n):
#     global count
#     count = 0
#     for i in range(1,31):
#         if i % n == 0:
#             print(i, end = " ")
#             count += 1
#     print(f'\n{n}의 배수의 개수: {count}')

# get_times(5)

    







