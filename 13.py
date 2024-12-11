# class

# a = dict()
# a = set()
# 위의 것들이 다 클래스 였다.

# class b:
#     pass
# bb = b()
# bb2 = b()
# bb3 = b()
# 클래스의 양식 이다.

# class Movie:
#     title = "소방관"
# movie1 = Movie()
# movie2 = Movie()

# print(movie2.title)
# print(movie2.title)

# movie1.title = "파묘"
# print(movie1.title)
# print(movie2.title)

# movie1.score = "1"
# print(movie1.score)
# # print(movie2.score)

# class Movie:
#     name = ''
#     def print_meg(msg):
#         print(msg)
#     def modify(self,movie):
#         self.name = movie
#     def print_name(self):
#         print(self.name)

# movie1 = Movie()
# movie2 = Movie()

# Movie.print_meg("print하기")
# # Movie.modify(movie1,"print하기2") # 이름을 print하기2 으로 설정.
# movie1.modify("프린트하기3") # 이름을 프린트 하기 3으로 설정.
# movie1.print_name() # 설정한 movie1의 이름을 출력.
# movie2.modify("프린트하기4")  # modify가 이름 설정
# print("movie2.name",movie2.name)

# class Movie:
#     def __init__(self):
#         print("Hello")

# movie = Movie() # __init__을 생성자라 한다.

# class Movie:
#     count = 0
#     def __init__(self, title, audience):
#         self.title = title
#         self.audience = audience
#         Movie.count += 1

# movie1 = Movie("파묘", 100)
# print(Movie.count) # 1
# movie2 = Movie("파묘2", 200)

# print(movie1.count)
# print(movie2.count)
# print(Movie.count)
# Movie.count += 1
# print(movie1.count) #3
# print(movie2.count)
# print(Movie.count)
# print(movie1.count)
# print(movie2.count)
# print(Movie.count)
# print(movie1.count)
# print(movie2.count)
# print(Movie.count)

#     # def __init__(self, title = "오징어 게임", audience = 300):
#     def __init__(self,title,audience):
#         self.title = title
#         self.audience = audience
    
# movie1 = Movie("파묘1",100)
# movie2 = Movie("파묘2",200)

# print(movie1.title,movie1.audience)
# print(movie2.title,movie2.audience)

# # movie3 = Movie()
# # print(movie3.title,movie3.audience)
# # # 내용이 꼭 있어야 한다.

# class Movie:
#     count = 0
    
#     def __init__(self, title, audience):
#         self.__title = title
#         self._audience = audience
#         Movie.count += 1

#     def get_title(self):
#         return self.__title
    
    # def set_title(self,title):
    #     self.__title = title

#     def get_audience(self):
#         return self._audience

# movie1 = Movie("파묘",100)
# # print(movie1.__title)
# print(movie1.get_title())
# # movie1.__title = "오겜"  #__로 되어있다면, 외부에서 접근이 안된다.(중요)
# # print(movie1.get_title())
# # print(movie1.__title)
# print(movie1._audience)
# print(movie1.get_audience())

# class MyAdd:
#     __a = 1
#     __b = 2
#     def sum(self):
#         return self.__a + self.__b
#     def set_a(self,a):
#         self.__a = a
# a = MyAdd()
# print(a.sum()) # 3
# # __a 값 3으로 변경 
# print(a.sum()) # 5


# # 왜인지 안된다. 아.. ()가 없는 오타가 있었다.
# class Health:
#     def __init__(self,name):
#         self.__name = name
#         self.__hp = 100

#     def get_name(self):
#         return self.__name
    
#     def set_hp(self, hp):
#         hp = max(hp,0)  # 0미만 일시 0이 더 크니 0으로 표기
#         hp = min(hp,100)  # 100 초과시 100이 더 작으니 100으로 표기
#         # if hp < 0:
#         #     hp = 0
#         # if hp > 100:
#         #     hp = 100
#         self.__hp = hp
    
#     def get_hp(self):
#         return "hp : " + str(self.__hp)

#     def exercise(self, hours):
#         self.set_hp(self.__hp + hours)
#         print(f"{hours}시간 운동하다")

#     def drink(self,cups):
#         self.set_hp(self.__hp - cups)
#         print(f"술을 {cups}잔 마시다")

# p1 = Health("나몸짱")
# p1.set_hp(100)
# p1.exercise(5)
# p1.drink(2)
# print(f"{p1.get_name()} - {p1.get_hp()}")

# p2 = Health("나약해")
# p2.set_hp(10)
# p1.exercise(1)
# p2.drink(12)
# print(f"{p2.get_name()} - {p2.get_hp()}")

# 실습 1 사칙연산 클래스 만들기
# 조건)
# 인스턴트를 생성할떄 2개의 숫자를 class에 보낸다.
# add 메서드는 두 수를 더한 결과값을 반환한다.
# sub 메서드는 두 수를 뺀 결과값을 반환한다.
# mul 메서드는 두 수를 곱한 결과값을 반환한다.
# div 메서드는 두 수를 나눈 결과값을 반환한다.

# class 사칙연산:
#     def __init__ (self,a,b):
#         self.__a = a
#         self.__b = b
#     def add(self):
#         return self.__a + self.__b
#     def sub(self):
#         return self.__a - self.__b
#     def mul(self):
#         return self.__a * self.__b
#     def div(self):
#         if self.__b == 0:
#             return "오류"
#         else: return self.__a / self.__b
        

# 입력 = 사칙연산(4,0)
# print(사칙연산.add(입력))
# print(사칙연산.sub(입력))
# print(사칙연산.mul(입력))
# print(사칙연산.div(입력))

# class Employee:
#     serial_num = 100

#     def __init__(self,name):
#         Employee.serial_num += 1
#         self.id = Employee.serial_num
#         self.name = name

#     def __str__(self):
#         return f"사번 : {self.id}, 이름 : {self.name}"

# e1 = Employee("최사원")
# print(e1)

# e2 = Employee("안사원")
# print(e2)

# e3 = Employee("한사원")
# print(e3)

# employee =[
#     Employee('구름'),
#     Employee('별'),
#     Employee('행성'),
#     Employee('달'),
# ]

# for i in employee:
#     print(i)
