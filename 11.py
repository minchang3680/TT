# add = lambda x,y : x+y
# print(type(add)) #함수도 변수에 집어넣을수 있다.
# print(add(1,2))

# def add2(x,y):
#     return x+y
# print(add2(1,2))

# add3 = add2
# print(add3(1,2))

# def call_3(func):
#     for _ in range(3):
#         func()

# call_3(lambda:print("hi"))
# call_3(lambda:print("hello"))

# def download(startCallback,endedCallback):
#     #download

#     endedCallback()
# download(lambda:print("다운로드 시작"),lambda:print("완료되었습니다."))

# list(map(int,['1','2','3']))

# result = map(lambda x:3*x, [1,2,3,4])
# print(list(result))

# li = [-5,1,2,-11,76]

# value = list(filter(lambda x:x>10,li))
# print(value) # [-5,-11]

# value = list(filter(lambda x:not x<0,li))
# print(value) # [-5,-11]

# value = list(filter(lambda x : x>3,map(lambda x:2*x,li)))
# print(value)

# arr = [1,2,3,100,99,98]
# nembers = []
# def solution():
#     for num in arr:
#         if num >= 50:
#             if num % 2 == 0:
#                 nembers.append(num/2) 
#             else:
#                 nembers.append(num*2) 
         
# solution()

# #어떤 문자열 a가 다른 문자열 b안에 속하면 a를 b의 부분 문자열이라 합니다.

# str1 = ("abc")
# str2 = ("aabcc")
# def solution():
#     for str1 in str2:
#         return 1
#     else:
#         return 0
# print(solution)

#문자열 myString이 주어집니다. myString을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 
# 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

# mystring = (int(input("입력")))
# def solution():
#     if 
    