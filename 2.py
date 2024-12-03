'''
print(3//2)
print(3.25//2)
print(3%2)
print(3.25%2)
print(2**3)
print(2**10)
print(1+2*3**2)
print(1+(2*(3**2)))
print(1+2*-3**2)
'''
# print("빵의 개수 :" ,30//4)
# print("남은 빵의 개수 :",30%4)

# a=1
# a+= 1 # a=1 a+1
# print(a)
# print("장원영"+"럭키비키")
# print("럭키"*10)
# # print("럭키"*"비키") 문자끼리 곱하면 에러가 난다.
# print("럭키"+"비키")
# song = input("너의 최애의 노래는?")
# print(song)
# print(type(song))
# print(2023-2010)
# years1 = 2023
# years2 = 2010
# print(years1-years2)

# while True:
#     lunch = input("오늘 점심 후보? ")
#     if lunch == "그만":
#         break
#     print(lunch + "!!")
# print('done')

# count = 0
# while True:
#     print(count)
#     if count == 5:
#         break
#     count += 1
# print("끝")

# num = 0
# while num < 10:
#     num = num + 1
#     if num % 2 != 0:
#         continue
#     print(num,end=" ")

# for 변수 in 리스트:
#     실행할 문장1
#     실행할 문장2
#     실행할 문장3
#     실행할 문장4
#     실행할 문장5
#     실행할 문장6

# shop = ["반팔","청바지","이어폰","키보드"]
# for i in shop:
#     print(i)

# a = range(10)
# print(list(a))

# b = range(1,11)
# print(list(b))

# c = range(1,10,2)
# print(list(c))

# for i in range(5):
#     print(i)


# for i in range(2,7):
#     print(i)

# for i in range(10,1,-1):
#     print(i,end=" ")

# for i in range(1,11):
#     print(i,end =" ")

# sum_val = 0
# for i in range(1,11):
#     sum_val += i
# print(f"\n합계 : {sum_val}")

#1부터 사용자가 입력한 수까지 정수의 합 계산
#번외) 홀수의 합만 구하기
# i = int(input("더해줄 정수를 입력하시오."))
# total1 = 0
# total2 = 0
# for num in range(1,i+1):
#     total1 += num
# print(total1)

# for num in range(1,i+1):
#     if num % 2 != 0:
#         total2 += num
# print(total2)

# # 실습2 입력한 숫자만큼 카운트 하고 "발사"출력
# 발사카운트 = int(input("발사 카운트를 설정해주세요 :"))
# for num in range(발사카운트,0,-1):
#     print(num)
# print("발사")

# # 구구단 만들기 - 사용자가 입력한 숫자의 구구단 출력
# 구구단 = (int(input("출력할 구구단을 입력하여주세요. :")))
# for num in range(1,10):
#     print(f"{구구단} * {num} = {구구단 * num}")

# # 점수 리스트 선언 및 생성
# score = [70,80,50,60,90,40]
# sum_v = 0
# for i in score:
#     sum_v += i

# count = len(score)
# avg = sum_v/count

# print("개수 :",count)
# print("합계 :",sum_v)
# print("평균 :",avg)

# #내장함수 sum()과 비교
# print("합계 :", sum([70,80,50,60,90,40]))
# print("합계 :", sum(score))

# [표현식 for 항목(요소) in 리스트]
a = [1,2,3,4,5]
a2 = []
a3 = []
a4 = []

#3의 배수로 저장
for i in a:
    a2.append(i*3)
print("a2 :",a2)

#리스트 내포
a3 = [i*3 for i in a]
print("a3 =",a3)

#3의 배수이면서, 짝수 인수 저장
a4 = [i*3 for i in a if i % 2 == 0]
print("a4 =",a4)