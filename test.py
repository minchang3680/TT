class Movie:
    count = 0
    
    def __init__(self, title, audience):
        self.__title = title
        self.__audience = audience
        Movie.count += 1

    def get_title(self):
        return self.__title
    
    # def set_title(self,title):
    #     self.__title = title

movie1 = Movie("파묘",100)
# print(movie1.__title)
print(movie1.get_title())
movie1.__title = "오겜"  #__로 되어있다면, 외부에서 접근이 안된다.(중요)
print(movie1.get_title())
print(movie1.__title)