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
# f.close()  # 종료.

f2 = open("text.txt")  # text.txt를 열고, ()안에 파일명, 뒤에 r(읽기)외에 다른것을 넣으면 오류가 난다.
print(f2.read())  # text.txt라는 파일을 끝까지 읽다. 숫자를 넣으면 그 인덱스 까지 읽는다
f2.close()# 종료  # 이 경우 5까지 읽어서 Hello World!! 에서 Hello 5까지 읽고 출력한 것이다.
# f = open("text.txt","a") # a는 추가.
# 근데 추가한게 유지는 안되네..
f2 = open("text.txt")
print(f2.readline())  
print(f2.readline(), end ="")  
print(f2.readline(), end ="")  
f2.close()