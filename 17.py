'''바이너리 파일'''
# with open("./output/data.bin","wb") as f:
#     txt = "안녕"
#     f.write(txt.encode())

# with open("./output/data.bin","rb") as f:
#     data = f.read()
#     print(data)
#     print(data.decode())

# with open("C:/Users/minch/Desktop/스크린샷 2024-11-26 000946.png",'rb') as f:
#     img = f.read()
# with open("./output/000946.png","wb") as f:
#     f.write(img)

'''에러처리'''
# try:
#     num = int(input("정수를 입력해주세요 :"))

# except ValueError:
#     print("정수가 아님!")
''''''
# try:
#     num = int(input("정수를 입력해주세요 :"))

# except ValueError as msg:
#     print(msg)

''''''
# try:
#     num = int(input("정수를 입력해주세요 :"))

# except Exception as msg:
#     print("정수가 아님!")
''''''
# try:
#     num = int(input("정수를 입력해주세요 :"))

# except Exception as msg:
#     print(msg)
''''''
# try:
#     num = int(input("정수를 입력해주세요 :"))

# except Exception as msg:
#     print(msg)
# else:
#     print("예외 없음")
'''
실습. 정수 입력 받기
사용자가 제대로 된 정수를 입력할 떄 까지 반복하여 입력 받기.
'''
# while True:
#     try:
#         number = int(input("정수를 입력하여주세요 :"))
#         print(f"정수 입력 성공 : {number}")
#         break
#     except ValueError:
#         print("정수가 아님! 정수를 입력해주세요!")
#     except Exception as msg:
#         print("정수가 아님! 정수를 입력해주세요!",msg)
'''finally'''
    # finally:
    #     print("무조건무조건이야")
'''raise'''
# try:
#     a = 1
#     if a > 1:
#         raise Exception
#     a += 1
#     print("a", a)
# except:
#     print("error", a)

'''raise #2'''
# class Cat(Animal):
#     def sleep(self):
#         print("고양이가 잠을 잔다")

#     def cry(self):
#         print("야~옹 야~옹")

''''''
class Animal:
    def breathe(self):
        print("숨을 쉰다")
    def cry(self):
        raise NotImplementedError
    
class Dog(Animal):
    def cry(self):
        print("멍멍")

d = Dog()
d.breathe()
d.cry()