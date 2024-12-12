# from modules.mylib import food # 동일 폴더 내에서만 가능함. C + 클릭 시에 해당 파일로 이동이 가능.

# print(food.name)
# food.cook()
# food.eat()

# from modules.mylib.food import cook, eat, name, mukbang

# print(name)
# cook()
# eat()


# import bbb.cm2
# print(bbb.cm2.add(1,2))

# f = open("text.txt","w")  #txet.txt 라는 파일에(없으면 새로 만들어서) w = 쓰다.  # 생성될떄 파일 권한이 없는 위치에는 만들수 없다. ex)사용자
# f.write('Hello World!!\n')  # Hello World라는 내용을 쓰다.
# f.close()  # 종료.

# f = open("text.txt","a")  
# f.write('Hello World22\n')
# f.write('bye\n')
# f.close()  # 종료.

# f2 = open("text.txt")  # text.txt를 열고, ()안에 파일명, 뒤에 r(읽기)외에 다른것을 넣으면 오류가 난다.
# print(f2.read())  # text.txt라는 파일을 끝까지 읽다. 숫자를 넣으면 그 인덱스 까지 읽는다
# f2.close()# 종료  # 이 경우 5까지 읽어서 Hello World!! 에서 Hello 5까지 읽고 출력한 것이다.
# f = open("text.txt","a") # a는 추가.
# 근데 추가한게 유지는 안되네..
# f2 = open("text.txt")
# print(f2.readlines())  
# print(f2.readlines(), end ="")  
# print(f2.readlines(), end ="")  
# f2.close()
# f4 = open("text.txt")
# print(f4.readlines())
# f4.close()

# f5 = open("text.txt", "r+")
# print(f5.read())
# print(f6.tell())
# f5.seek(4)  # 4번 자리로 돌아가라.
# print(f5.write("8"))  # 그래서 4번자리에 8이 입력되어 들어감. ex) Hell8 World!!
# f5.close()

# f6 = open("text.txt","r+")
# str6 = f6.read()
# print(f6.tell())
# f6.seek(str6.find('5')) # 5가 있는 위치를 찾아서 돌아간다,
# print(f6.write("8")) # 그리고 그 위치에 8을 집어 넣는다. before) 12345678 -> after) 12348678
# f6.close()

# with open("text.txt","r+") as f7:
#     str6 = f7.read()
#     print(f7.tell())
#     f7.seek(str6.find('3')) # 5가 있는 위치를 찾아서 돌아간다,
#     print(f7.write("8")) # 그리고 그 위치에 8을 집어 넣는다. before) 12345678 -> after) 12348678


