# # 문제1.
# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
#     if not answer:
#         answer.append(-1)
#     answer.sort()
#     return answer

# print(solution([2, 36, 1, 3],1))

# # arr % drivisor은 안되네..
# # 왜 if not answer로 해야되지?
# # answer.sort() = .sort에 ()괄호를 넣지 않으면.. 안되는구나.

# # 문제 2
# # 입력 값을 넣고, 그 입력값을 더했을떄 나올수 있는 모든 경우의 수를 출력하라.
# def solution(numbers):
#     answer = []  # 중복을 제거할 set을 사용
#     # 기존 값 중 2보다 크거나 같은 값을 먼저 set에 추가
#     for num in numbers:
#         if num >= 2:
#             answer.append(num)
    
#     # 리스트의 각 원소에 대해 자기 자신을 제외한 다른 원소들과 합치기
#     for i in range(len(numbers)): # nember의 길이 횟수만큼 반복.
#         for j in range(len(numbers)): # 마찬가지
#             if i != j:  # 단, 동일한 경우 제외.
#                 answer.append(numbers[i] + numbers[j])  # 합을 set에 추가 (중복 자동 제거) # 아 이부분이 대체 모르겠따.
    
#     return list(set(answer))  # 결과를 리스트로 변환하여 반환

# print(solution([2,1,3,4,1]))

# print(1 if 1<0 else 0) # 이런것도 가능하다. if가 해당되면, 왼쪽 결과가 나오고 아니라면 오른쪽 결과가 나온다.

# print("abc" if 1<0 else "bcd")
# #     if 결과 , 조건문, else 결과
# if 1<0:
#     print("abc")
# else:
#     print("bcd")

# #문제3
# def solution(x):
#     a = sum(list(map(int,str(x))))
#     if x % a == 0:
#         return True
#     else:
#         return False

# print(solution(11))

# # 문제 4
# def solution(s):
#     list = sorted(s, reverse=True)
#     answer = ''
#     for i in range(len(list)):
#         answer += list[i]
#     return answer

# print(solution("Zbcdefg"))

# # 문제 4
# def solution(s):
#     list = sorted(s, reverse=True)  # 순서를 거꾸로 하기. # 다만 대문자는 왜 순서가 그렇게 된지는 모르겠음.
#     a = "".join(list) # list나 튜플이라거나 이런 경우에는 str(스트링[문자형])으로 변경하려면 join을 써줘야 한다.
#     return a

# print(solution("Zbcdefg"))

# # 문제5
# # 총 추억 점수는 photo , yearning = 점수, name = 이름. 
# # 딕셔너리를 활용하는 것 같은데.. name과 yearning를 키와 값으로 묶어서 쓰는거 같은데.., 참.
# def solution(name, yearning, photo):
#     answer = []  # 빈 리스트로 초기화
#     photo_dict = {}  # photo 딕셔너리로 이름과 yearning 매핑
    
#     for i in range(len(name)):  # name의 길이만큼 반복
#         photo_dict[name[i]] = yearning[i]  # name[i]를 키로, yearning[i]를 값으로 매핑
    
#     # photo 리스트에서 각 그룹에 대해 yearning 값 합산
#     for group in photo:
#         total = 0
#         for person in group:
#             if person in photo_dict:  # photo_dict에 해당하는 사람이 있다면
#                 total += photo_dict[person]  # 해당 사람의 yearning 값을 더함
#         answer.append(total)  # 각 그룹의 yearning 합을 answer에 추가
    
#     return answer  # 결과 반환

# print(solution(["may", "kein", "kain", "radi"],
#                [5, 10, 1, 3],
#                [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))

# 문제 6
# 아 그 나누는 기준 정해서 하는 그거.. x하던거.. = .split(나누는 기준.)
def solution(t, p):
    answer = []
    list = t.split(p)
    print(list)
    # for i in list:
    #     answer.appened(lne(i))
        
    return answer
print(solution("3141592","271"))