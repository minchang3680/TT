# print(True and False) # &&
# print(True or False) # 
# print(not True)
#print(!True)
# cart = ["계란", "마늘","콩나물","커피"]
# print("두부" in cart)
# print("계란" in cart)
# if 1<3:
#     print("True")
#     print("True")
# print("False")

# a = int(input("숫자를 입력하시오. :"))
# if (a%2==0):
#     print("짝수")
# else :
#     print("홀수")
# a = int(input("숫자를 입력하시오. :"))
# if (a % 2 == 0):
#     print("짝수")
# else:
#     print("홀수")

# a = int(input("점수 :"))
# if 90<a<=100:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=70:
#     print("C")
# elif a>=60:
#     print("D")
# elif 60>a:
#     print("E")
# score = int(input("점수: "))
# if score < 60:
#     print("E")
# elif score < 70:
#     print("D")
# elif score < 80:
#     print("C")
# elif score < 90:
#     print("B")
# else: print("A")
# if score>100:
#     print("100점 이상은 없습니다.")
# years = int(input("나이를 입력하세요:"))
# money = input("'카드'또는 '현금'만 입력 :")
# if years < 8:
#     print(f"{years}세의 요금은 무료입니다.")
# elif 8<years<14:
#     print(f"14세 미만의 {money}요금은 450원입니다")
# elif years < 20:
#     if money == "카드":
#           print (f"{years}세의 {money}요금은 720원입니다.")
#     else :
#             print(f"{years}세의 {money}요금은 1000원입니다.")
# elif years < 75:
#     if money == "카드":
#             print (f"{years}세의 {money}은 1200원 입니다.")
#     else :
#         print(f"{years}세의 {money}요금은 1000원입니다.")
# else:
#     print(f"{years}세의 요금은 무료입니다.")

# 1
# vending_machne = ['게토레이','레쓰비','생수','이프로']
# 음료 = input("마시고 싶은 음료? :")
# if 음료 in vending_machne:
#     print(f"{음료} 드릴게요")
# else : 
#     print(f"{음료}는 지금 없네요.")

2
vending_machne = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']
user = input('소비자와 주인 가운데 입력하세요 :')

if user=="소비자":
    음료 = input("마시고 싶은 음료? :")
    if 음료 in vending_machne:
        print(f"{음료}드릴게요.")
        vending_machne.remove(음료)
    elif 음료 not in vending_machne :
        print(f"{음료}는 없는 음료입니다.")
    

elif user =="주인":
    추가삭제 = input('추가 혹은 삭제 가운데 선택하여주세요.')    
    if 추가삭제 == "추가":
        추가음료=input("추가할 음료를 입력하여주세요.:")
        index=vending_machne.index(추가음료)  #해당 동일한 추가음료의 위치를 찾는다.
        vending_machne.insert(index,추가음료)  #찾은 위치에 동일 해당음료를 넣는다.
    else:
        추가삭제 == "삭제"
        삭제음료 = input("삭제할 음료를 입력하여주세요.:")
        if 삭제음료 in vending_machne:
            vending_machne.remove(삭제음료)
        else: print(f"{삭제음료}는 현재 없습니다.")
print(vending_machne)
      



    