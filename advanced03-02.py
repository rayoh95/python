# 시퀀스형
# 헤시테이블(hashtable) -> 파이썬 내장 엔진. 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

from unicodedata import name
from dis import dis
from types import MappingProxyType
import csv

# Dict 구조
print('Ex1-1 : ')
# print(__builtins__.__dict__)

print()

# Hash 값 확인 -> 중복의 허용에 대해
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print('Ex1-2 : ', hash(t1))
# print('Ex1-3 : ', hash(t2))  # hash 값이 나오지 않고 에러발생

print()

# 지능형 딕셔너리(Comprehending Dict)

# 외부 CSV TO List of tuple
with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print('Ex2-1 : ',)
print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()

print('Ex2-2 : ',)
print(n_code1)
print()
print('EX2-3 : ',)
print(n_code2)

# Dict Setdefault 예제

source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No user setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print('Ex3-1 : ', new_dict1)

# User setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print('Ex3-2 : ', new_dict2)


# 사용자 정의 dict 상속(UserDict 가능)

class UserDict(dict):
    def __missing__(self, key):
        print('Called : __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, defualt=None):
        print('Called : __getitem__')
        try:
            return self[key]
        except KeyError:
            return None

    def __contains__(self, key):
        print('Called : __contains__')
        return key in self.keys() or str(key) in self.keys()


user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one': 1, 'two': 2})
user_dict3 = UserDict([('one', 1), ('two', 2)])

# 출력
print('Ex4-1 : ', user_dict1, user_dict2, user_dict3)
print('Ex4-2 : ', user_dict2.get('two'))
print('Ex4-2 : ', 'one' in user_dict3)
# print('Ex4-4 : ', user_dict3['three'])
print('Ex4-5 : ', 'three' in user_dict3)

print()

# immutable Dict


d = {'key1': 'TEST1'}

# Read Only
d_frozen = MappingProxyType(d)

print('Ex5-1 : ', d, id(d))
print('Ex5-2 : ', d_frozen, id(d_frozen))
print('Ex5-3 : ', d is d_frozen, d == d_frozen)

# d_frozen['key1'] = 'TEST2'    # 수정 불가능한 객체라 에러가 난다.

d['key2'] = 'TEST2'

print('Ex5-4 : ', d)

print()

# Set 구조(FrozenSet)

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()  # 빈 set 을 선언하는 방법. s4={} 는 빈 딕셔너리 선언이다.
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s2.add('Melon')

# 추가 불가
# s5.add('Melon')

print('Ex6-1 : ', s1, type(s1))  # hash 가 더 중요하기 때문에 순서는 바뀐다. 중복은 알아서 빼서 출력
print('Ex6-2 : ', s2, type(s2))
print('Ex6-3 : ', s3, type(s3))
print('Ex6-4 : ', s4, type(s4))
print('Ex6-5 : ', s5, type(s5))

# 선언 최적화

a = {5}
b = set([10])
# 어떤 선언 방법이 더 빠를까?

print('Ex6-5 : ')
print(dis('{10}'))
print('Ex6-6 : ')
print(dis('set([10])'))

print()

# 지능형 집합(Comprehending Set)

print('Ex7-1 : ')
print({name(chr(i), '') for i in range(0, 256)})
