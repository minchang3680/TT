# i = 0
# while i<5:
#     i+=1
#     print("안녕하세요",i)
# print('끝')

# while True:
#     lunch = input("오늘 점심 후보? ")
#     print(lunch + "!!")
# print('done')

# num = 0
# while num < 10:
#     num = num +1
#     if num %2 != 1:
#         continue
#     print(num)

# while True:
#     lunch = input("오늘 점심 후보 :")
#     if lunch == "그만":
#         break

# #1부터 사용자가 입력한 수까지 정수의 합 계산
# #번외) 홀수의 합만 구하기.
# i = int(input("합계를 구할 정수를 입력하여 주세요.: "))
# total_1 = 0
# total_2 = 0
# for num in range(1,i+1):
#     total_1 += num
#     if num % 2 != 0 :
#         total_2 += num
# print(total_1)
# print(total_2)

# 실습2 입력한 숫자만큼 카운트 하고 "발사"출력
# i = int(input("발사 카운트를 입력하여 주십시오. :"))
# for num in range(i,0,-1):
#     print(num, end=" ")
# print("발사")

# 구구단 만들기 - 사용자가 입력한 숫자의 구구단 출력
nember = int(input("출력할 구구단의 단수를 입력하여주세요. :"))
for num in range(1,10):
    print(f"{nember} * {num} = {nember * num}")

# a=[10,20,30]
# print(sum(a)) #sum 은 합계를 구해준다.
# print(sum(a)/len(a)) #len은 길이 = 3 합계 / 길이(3) 60 / 3 = 20

# a = [1,2,3,4,5,]
# a2=[]
# a3=[]
# a4=[]

# for i in a:
#     a2.append(i*3)
# print("a2 =",a2)

# a3 = [i*3 for i in a]
# print("a3 =",a3)

# a4 = [i*3 for i in a if i%2 == 0]  #i*3 한것들 가운데 만약 i%2의 나머지가 0일 떄(in) 출력한다.
# print("a4 =",a4)  # 따라서 i * 3 = 3 6 9 12 가운데 나머지가 2로 나누었을떄 나머지가 0인 6과 12만 출력된다.

# for y in range(3): #외부반복문
#     for x in range(2):
#         print(f"y: {y}, x: {x}")
#     print()

# for i in range(2,10):
#     print(f'[{i}단]')
#     for j in range(1,10):
#         print(f'{i} x {j} = {i*j}')
#     print()


# print('*** 자리배치도 ***')
# customer = int(input('고객수 입력: '))
# column = int(input('좌석열 수 입력: '))  #열수

# if customer % column == 0:
#     row = customer // column
# else:
#     row = (customer // column) + 1
# # print(row)

# for i in range(0, row):
#   for j in range(1, column + 1):
#     seat = i * column + j
#     if seat > customer:
#       break
#     print(seat, end=" ")
#   print()

# # # 별찍기 - 아래와 같이 출력이 되도록 코드를 작성.
# # #1 
# i = int(input("몇 층까지 쌓겠습니까? :"))
# print("#1")
# for j in range(0,i+1):
#     print(j*"*")
# print("#2")
# #2
# for j in range(0,i+1):
#     print((j*"*").rjust(i))
# print("#3")
# #3
# for j in range(1, i + 1):
#     print(((j * 2 - 1) * "*").center(i * 2 - 1))

# 리스트 평균 구하기
# 1. 여러개의 숫자를 입력받아 리스트를 만든다.
# 2. 제일 큰 수와 제일 작은 수를 찾고
# 3. 그 두개를 뺸 나머지 값들의 평균 구하기
# (리스트 만들떄, 공백을 기준으로 문자열을 쪼개 리스트 만들 것!)
#  +힌트: 최대/최소값 : max(),min()

#여러개의 숫자를 입력받아 리스트를 만든다.
# num_list = list(map(int,input("숫자를 입력:").split()))
# num = list(map(int,input("숫자를 입력하세요.: ").split()))
# print(type(num))
# max_num = max(num)
# print("가장 큰 값: " ,max_num)
# min_num = min(num)
# print("가장 작은 값: ",min_num)
# num.remove(max_num)
# num.remove(min_num)
# ave = sum(num)/len(num)
# print("나머지 값의 평균 : ",ave)