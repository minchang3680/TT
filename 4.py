# a =[]
# b =[1,2,3,4]
# c = ["장원영","아이브"]
# d = [1,"장원영"]
# # print(len(c))
# # print(c[0]) #0부터 시작한다.
# # print(c[1])
# # c[0] = "카리나"
# # print(c)
# # del c[0]
# # print(c)
# # c.append("asdfs")
# # print(c)
# print(b[-1])
# print(b[-2])
# print(type(b))

# 슬라이싱
# # [0:n] -> n-1 위치
# seasons = ["봄","여름","가을","겨울"]
# print(seasons[0:1])
# print(seasons[0:2])
# print(seasons[:2])
# print(seasons[1:])
# print(seasons[2:])
# print(seasons[1:3])
# print(seasons[::2])
# print(seasons[::3])
# print(seasons[::-1])

# seasons2 = ["봄","여름","가을","겨울",[1,2,3,4]]
# print(seasons2[-1][0])
# print(seasons2[-1])
# shop = ["반팔","청바지","이어폰","키보드"]
# shop[0] = "무지 반팔"
# del shop[2:4]
# print(shop)
# abcd = "abcd"
# ['a','b','c','d']
# print(len(abcd))

# a = [1,2,3,4,5,6,7,8,9,10]
# even = a
# print(even[1::2])
# a.sort()
# # a.reverse() a[::-1]
# print(a)
# b=["a","b","c","d",]
# b.sort()
# print(b)
# c=["1","10","2"]
# c.sort()
# print(c)
d = ["강남","강북","서","게임","서","서"]
first = d.index("서")+1
print(d.index("서"))
print(first + d[first:].index("서"))
print(d.count("서"))
# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
# print(rainbow[2])
# rainbow.sort()
# print(rainbow)
# skyblue ="skyblue"
# rainbow.append(skyblue)
# print(rainbow)
# del rainbow[3:7]
# print(rainbow)