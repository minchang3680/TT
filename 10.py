# def pr_str(txt, count=1, count2=1):
#     for i in range(count):
#         print(txt)
#         print(count2)

# pr_str("Hello", 3, 2)
# pr_str("Hello", 3)
# print()
# pr_str("Hello")
# print()
# pr_str() #txt='12'

# def calc_avg(*numbers):  # *을 붙여야 가변 매개변수가 된다.
#     print(type(numbers))
#     return sum(numbers)/len(numbers)  #sum 모두 더하기 / len 총길이

# print(calc_avg(1,2))
# print(calc_avg(1,2,3,4,5))

# def a():
#     return 1,2

# print(a())

# def intro(**kw):
#     print(type(kw))
#     for k, v in kw.items():
#         print(f"{k}: {v}")

# intro(name = "Alice",age = 25, city="NY")

# list = [2,4,1,4,6]
# list.sort()
# print("list: ",list)
# list2 =[2,4,1,4,6]
# print("list2: ",sorted(list2))
# print("list2: ",list2)

# # 3번쨰로 작은 값의 인덱스를 구하라.
# list.sort()
# a = list.index(3)
# print(a)

# print(eval("1+2*3"))
# print(int(4.6+0.5))
# print(int(4.4+0.5))
# print(round(4.6))
# print(round(4.4))

# print(round(2.547))
# print(round(2.547,1))
# print(round(2.547,2))
# print(round(127,-1))
# print(round(127,-2))
# print(round(127))

# print(2**3)
# print(pow(2,3))

# count = 0
# def hello():
#     global count
#     print("hello")

#     count += 1
#     if count == 3:
#         print("stop")
#         return
# hello()
        

# hello()
# print("stop")

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# # 실습 2. 재귀 함수로 피보나치 수 구하기.
# def fi(n):
#     if n <= 2:
#         return 1
#     else:
#         return fi(n-2) + fi(n-1)
# print(fi(1))
# print(fi(5))

# def fi(n):
#     if n <= 2:
#         return 1
#     a, b = 1, 1  # 피보나치 수열의 첫 번째와 두 번째 값
#     for _ in range(3, n+1):
#         a, b = b, a + b  # 이전 두 값을 더하여 피보나치 수를 계산
#     return b

# def fi(n, memo={}):
#     if n <= 2:
#         return 1
#     if n not in memo:  # 이미 계산한 값이 없다면
#         memo[n] = fi(n-1, memo) + fi(n-2, memo)  # 값 계산 후 메모에 저장
#     return memo[n]  # 메모에 저장된 값 반환

# print(fi(1))  # 1
# print(fi(50))  # 12586269025 (빠르게 계산됨)

# def fibo(b):
#     return fibo(b-2) + fibo(b-1)
# print(fibo(1))
# print(fibo(3))

# # 하노이의 탑
# def hanoi(number_of_disks_to_move, from_, to_, via_):
#     if number_of_disks_to_move == 1:
#         print(from_, "->", to_)
#     else:
#         hanoi(number_of_disks_to_move-1, from_, via_, to_)
#         print(from_, "->", to_)
#         hanoi(number_of_disks_to_move-1, via_, to_, from_)

