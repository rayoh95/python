#딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json) -> MongoDB

#선언
a = {'name' : 'Kim', 'Phone' : '010-7777-7777', 'birth' : 870214}
b = {0: 'Heool Python', 1: 'Hello Coding'}
c = {'arr' : [1, 2, 3, 4, 5]}

print(type(a))
print(a['name'])
print(a.get('name'))
print(a.get('address')) #에러가 안 난다.
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3,)


# keys, values, items
print(a.keys())
print(type(a.keys()))
print(list(a.keys()))

print(a.values())

print(a.items())


# 집합(Sets) : 순서x, 중복x
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)    # 중복 허용x

t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2))  #교집합
print(s1 & s2)  #교집합

print(s1 | s2)
print(s1.union(s2)) #합집합


# 추가 & 제거
s3 = set([7,8,10,15])

s3.add(18)

s3.remove(15)
print(s3)
