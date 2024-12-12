import sys

# print(sys.argv)  # 특정 경로에 입력값을 추가해주는.

# args = sys.argv[1:]
# print(type(args))

# print(int(sys.argv[1]) + int(sys.argv[2]))

# # 실습
# args = sys.argv[1:]
# total = 0
# for i in args:
#     total += int(i)

# print(total)

# print(sum(map(int,sys.argv[1:])))

#실습
# args = sys.argv
# print(args)
# if len(args) > 4 or len(args) <= 2:
#      print("오류")
#      sys.exit()
# if args[1] == "add":
#      print(f"add {int(args[2]) + int(args[3])}")
# elif args[1] == "mul":
#      print(f"mul {int(args[2]) * int(args[3])}")

# 리더님
# import sys

# args = sys.argv
# if (len(args)!=4):
#     print("입력오류")
#     sys.exit(0)  # 에러가 나면 바로 종료하도록.
# else :
#     cmd = args[1]
#     num1 = int(args[2])
#     num2 = int(args[3])
#     if cmd == "mul":
#         print(num1*num2)
#     elif cmd == "add":
#         print(num1+num2)

import os

# os.chdir("C:\\Users\\minch\\TT")  # 디렉터리 경로
# dir = os.popen('dir') # dir 명령으로 열기
# print(dir.read()) # 디렉터리 보기(읽기)

# print(os.listdir()) # 파일을 리스트에 저장.
# # 경로에 이스케이프 문자(\)를 각각 하나씩 넣어줘야 제대로 인식한다. C:\Users\minch\TT의 경우 불가.

# 영타 연습 프로그램

import random
import time
import os

n = 1
# word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#         'grape', 'garlic', 'onion', 'potato']

# if os.path.exists(): # 파일이 있는지 확인.
#     with open("word.txt","r") as f:
#         word = f.read().split()
# else :
#     word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#         'grape', 'garlic', 'onion', 'potato']


input("*[타자게임] 준비되면 엔터*")
start = time.time()

while n < 11:
    print("문제",n)
    question = random.choice(word)   # choice는 중복이 가능함 
    print(question)
    user = input()
    if question == user:
        print("통과")
        n += 1
    else:
        print("오타! 다시 도전!")

end = time.time()
et = end - start
print(f'타자시간: {et:.2f}초')  # 2f가 소수점 몇번쨰 자리 까지 확인하는지.
# .?f로 표기 해야된다.