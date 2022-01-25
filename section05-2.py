# 사퀀스(순서가 있는)자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range 함수, reverse 함수, enumerate 함수, filter 함수, map 함수, zip 함수

names = ['kim', 'park', 'cho', 'choi', 'yoo']

for name in names:
    print("you are : ", name)

word = 'dreams'

for s in word:
    print(s)


my_info = {
    "name" : "Oh",
    "age" : 27,
    "city" : "Seoul"
}

for key in my_info:
    print("my_info: ", key)

for key in my_info.keys():
    print("my_info: ", key)

for value in my_info.values():
    print("my_info: ", value)

for k, v in my_info.items():
    print("my_info: ", k, v)


