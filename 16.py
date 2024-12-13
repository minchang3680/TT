# # 리스트 랜덤 출력.

# import random
# with open("word.txt","w") as f:
#     word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#         'grape', 'garlic', 'onion', 'potato']
#     for i in word:
#         f.write(i + ' ') # ' ' =  \n,\t,\r 등도 가능

# with open("word.txt", 'r') as f:
#     # date = f.readlines() # \n으로 했을 경우에 이렇게도 가능하다.
#     date = f.read().split() 
#     word = random.choice(date)
#     print(word)

# import sys

# with open("./output/input.txt",'a') as f:  # a   :  파일의 뒷부분에 데이터를 추가하기 위해 파일을 연다.
#     while True:
#         text = input("저장할 내용 입력(종료-z)")
#         if text == 'z' or text == 'z':
#             # break
#             sys.exit(0)
#         f.write(text + '\n')

''' 실습 회원 명부 작성하기.'''

# with open("./output/member.txt",'w',encoding='utf-8') as f:
#     for i in range(3):
#         name = input("이름을 입력하세요 :")
#         pw = input("비밀번호를 입력하세요 :")
#         print(f"이름 : {name}\t비밀번호 : {pw} \n")
#         f.write(f"{name}\t{pw} \n")  # 내가 만든 member.txt에 쓰는 내용.

# with open("./output/member.txt",'r',encoding='utf-8') as f:
#     print(f.read())  # 내가 메모장에 write 한 내용이 나온다.

'''       
실습2) 회원 명부를 이용한 로그인 기능.
이름을 입력하세요 라는 메세지를 출력한 뒤 이름 입력 받기
사용자에게 비밀번호를 입력하세요 라는 메세지를 출력한 뒤 비번 입력 받기
member.txt 에서 한줄씩 "이름"과 "비번"을 검사하여 로그인 성공시 "로그인 성공" 실패시 "로그인 실패" 출력
여기서 member.txt 앞 실습에서 사용한 회원 명부 사용
'''
# with open("./output/member.txt","r",encoding="utf-8") as f:
#     name_check = input("이름을 입력하세요. : ")
#     pw_check = input("비밀번호를 입력하세요. : ")
#     for i in f:
#         n, p = i.split()  # member.txt에 든 내용을 split으로 n,p에 각각 list화 하겠다. 단, 띄어쓰기를 기준으로 나누는 듯 함.
#         if name_check in n and pw_check in p:
#             w="로그인 성공"
#             break
#         else:
#             w="로그인 실패"
# print(w)  # 로그인 성공시에만 출력.      

'''
# 회원 찾기 시에 한번에 찾도록 업그레이드.
# 딕셔너리 활용.
'''
# dictUser = {}

# with open("./output/member.txt", 'r',encoding = "utf-8") as f:
#     for line in f:
#         n, p = line.split()
#         dictUser[n] = p

# print(dictUser)

# # for i in range(100) :
# name = input("이름을 입력하세요: ")
# pw = input("비밀번호를 입력하세요: ")

# if pw == dictUser.get(name):  
#     print("로그인 성공!")
# else:
#     print("로그인 실패!")

'''    
if pw == dictUser.get(name):  
이 딕셔너리 가운데 내가 입력한 name과 동일 한 것을 찾아서 pw가 동일한지 확인하는 것
'''

'''
실습3 로그인 성공시 전화번호 저장하기.
1. 로그인 성공시, 사용자에게 "전화 번호를 입력하세요."라는 메세지를 출력한뒤 전화번호 입력받기.
2. 사용자로부터 입력 받은 전화번호를 이름과 함께 member.txt에 기록
3. 새로운 사람이 로그인 성공시에 member.txt에 전화번호 추가하기.
4. member.txt에 이미 존재하는 사람이 로그인 성공시 전화번호 수정하기.
'''

dict_users = {}
dict_phone={}
with open("./output/member.txt","r",encoding="utf-8") as f:
    for i in f:
        n, p = i.split()
        dict_users[n] = p
with open("./output/member_tel.txt","r",encoding="utf-8") as f:
    for i in f:
        n, p = i.split()
        dict_phone[n] = p


name = input("이름을 입력하세요. : ")
pw = input("비밀번호를 입력하세요. : ")

if pw == dict_users.get(name):
    print("로그인 성공")

    with open("./output/member_tel.txt","w",encoding="utf-8") as f:
        number = input("전화번호를 입력하세요. : ")
        dict_phone[name]=number
        for name,phone in dict_phone.items():
            f.write(f"{name}\t{phone}\n")
     
else:
    print("로그인 실패")

''' 매번 초기화 '''

