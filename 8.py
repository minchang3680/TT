# t1 = (10,20,30)
# print(type(t1))
# print(t1)
# print(t1[0])
# # del t1[0]이런거 안된다.
# #요소가 한개인 튜플 생성
# t2 = (10)
# print(t2)
# t3 = (10, )
# print(t3)
# t4 = 10,20
# print(t4)
# print(type(t4))

# # 셋 만들기
# numbers1 = {1,2,3,4,5}
# print(numbers1)
# numbers2 = {1,2,3,4,5,5}
# print(numbers2)
# apple = set('apple')
# print(apple)

# # 값 in 셋
# print(1 in numbers1)
# # #값 not in 셋
# print("c" in apple)

# # 요소 추가
# numbers1.add(6)
# print(numbers1)

set1 = {1,2,3}
print(set1)
set2 = set({1,2,3,3})
print(set2)
set2.add(4)
print(set2)
while len(set2) > 0:
    a = set2.pop()
    print(a)

l1 = [1,2,3,4]
while len(l1) > 0:
    a = l1.pop()  #pop되는 것은 랜덤인가?
    print(a)

# set3 = set("apple")
# print(set3)
# while len(set3) > 0:
#     a = set3.pop()
#     print(a)

# 셋(set)의 교집합
# & = 교집합
# .intersection()

# 셋의 합집합 
# | = 합집합
# .union()

# 셋의 차집합
# - = 차집합
# .difference

#셋 응용 - 중복이름 찾기

# name = ["흥부","콩쥐","놀부","콩쥐"]
# dupl_name = set()
# print(dupl_name)
# n = len(name)
# for i in range(0,n-1):
#     for j in range(i+1, n):
#         if name[i] == name[j]:
#             dupl_name.add(name[i])
# print("중복 이름: ",dupl_name)

# names = ["1","2","3","2"]
# for i in range(len(names)):
#     if names.count(names[i]) > 1:
#         print(names[i])
# names_set = set(names)
# print(names_set)
# names_list = list(names_set)
# names_list.sort()
# print(names_list)

# # for루프 이용해서 중복 제거하기
# name = ["1","2","3","2"]
# a = []
# for i in range(len(name)):
#     if a.count(name[i]) < 1:
#         a.append(name[i])
# name = a
# print(name)

# name = ["1","2","3","2"]
# a = []
# for i in range(len(name)):
#     if name.count(name[i]) >1:
#         name_1 = list(name)
#         name_1.remove([i])
# name = set(name_1)
# print(name)
# # 찬국형이 짠 이코드는 그나마 이해가 되는데 말이지..
# # 근데 이렇게 하면 동일한 것을 더 추가했을떄 여전히 중복이 되서 안된다네..?

# a ={}
# print(type(a))
# b = {1}
# print(type(b))
# c = dict()
# c = {1:'a','b':'b'}
# print(c)
# c[2] = 'c'
# c['c'] = 2
# print(c)
# del c[2]
# del c['b']
# print(c)
## print(c[2]) # error
# print(c.get(2)) # none

# # print(c.get(2))
# print(c.keys())  #키
# print(c.values()) # 값

# for i in c.keys():
#     print(i, c.get(i))

# print('c' in c) # print('c' in c.keys()) 이렇게 하면 안된다.
# print(2 in c.values())

# try / except 쓰지 않고 출력 및 에러처리
# dic = {
#     "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
#     "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
#     "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
# }
# print("★ 컴퓨터 사전 ★")
# word = input("검색할 단어를 입력하세요: ")
# if word in dic:
#     print(f'{word}: {dic[word]}')
# else:
#     print("정의된 단어가 없습니다.")

# value = dic.get(word)
# if value:
#     print(f'{word}:{dic}')

# # 실습) 
# import sys
# input = sys.stdin.readline
# a,b = map(int,input("리스트를 입력해주세요. :").split())  #a와 b는 사용자가 처음에 입력한 값에 의해 결정됩니다.
# a_str = set()  # a_str = set라는 셋을 설정
# for i in range(a):  # a개의 문자열을 입력 받고, 그 값을 셋인 a_str에 추가.
#     a_str.add(input())  # a_str에 a의 내용을 추가.
# count = 0  # count = 0으로 설정
# for i in range(b):  # b개의 문자열을 입력받고 
#     str = input()  # str에 입력
#     if str in a_str:  #만약 a_str에 str이 겹치는 부분이 있다면..
#         count += 1  # count를 1씩 더해준다.
# print(count)  #총 카운트를 출력한다.

# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# S = set()
# for i in range(N):
#     S.add(input())
# ans = 0
# for _ in range(M):
#     t = input()
#     if t in S:
#         ans+=1
# print(ans)  #30분 안에 풀수 있어야 한다고 함.

# 실습 2) 딕셔너리 사용
# 1. 학생들의 점수를 저장하는 학생 딕셔너리를 생성한다.
# 2. "Alice","Bob","Charlie" 세명의 학생을 key로 갖고, 
# 각각의 점수를 85, 90, 95를 value로 갖는 데이터를 추가한다.
# 3. 학생 추가 : "David" 학생의 점수로 80을 추가한다.
# 4. 학생 점수 수정: "Alice"학생의 점수를 88로 수정한다.
# 5. 학생 삭제 :"Bob"학생을 딕셔너리에서 삭제한다.
# 6. 학생 전체 출력 : 딕셔너리에 있는 모든 학생과 점수를 출력한다.(for문 이용)

# dict = {"Alice" :85, "Bob" :90, "Charlie" :95}
# print(dict)
# dict["David"] = 80
# print(dict)
# dict["Alice"] = 88
# print(dict)
# del(dict["Bob"])  # pop를 쓴다면 value가 남는다.
# print(dict)
# for i in dict:
#     print(f"{i} : {dict[i]}",end = " ")

# 딕셔너리 응용

# # 2차원 리스트
# d = [
#     [10,20],
#     [30,40],
#     [50.60]
# ]
# print(d)

# print(d[0][0])
# print(d[1][1])
# d.append([70,80])
# print(d)

# d[0][0] = 90
# print(d)

# # d[1].pop(0)
# # del(d[1][1])
# print(d)
# print(len(d))
# print(len(d))

# for i in range(0,len(d)):
#     for j in range(0,len(d[i])):
#         print(d[i][j],end=" ")
#     print()

# for x, y in d:
#     print(x,y)