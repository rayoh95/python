# 흐름제어, 병행처리(Concurrency)
# 제네레이터, 반복형
# Generator

# 파이썬 반복형 종류
# for, collections, text file, List, Dict, Set, Tuple, unpacking(*), *args
# 반복형 객체 내부적으로 iter 함수 내용, 제네레이터 동작 원리, yield from

import itertools
from collections import abc

# 반복 가능한 이유? -> iter() 함수를 호출하여 사용하는 것.

t = 'ABCDEF'

# for 사용
for c in t:
    print('Ex1-1 : ', c)

print()

# while 사용

w = iter(t)

while True:
    try:
        print('Ex1-2 : ', next(w))
    except StopIteration:
        break

print()

# from collections import abc

# 반복형 확인
print('Ex1-3 : ', hasattr(t, '__iter__'))   # t 가 iter 라는 속성을 가지고 있는지 확인하는 함수
# t 가 abc의 Iterable 과 같은 인스턴스인지 확인하는 함수
print('Ex1-4 : ', isinstance(t, abc.Iterable))
# dir 로 찍어서 iter 을 확인할 수도 있다.
print()


# next 사용

class WordSplitIter():
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('stop!')
        self._idx += 1
        return word

    def __iter__(self):
        print('Called __iter__')
        return self

    # 매직 메소드
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitIter('Who says the nights are for sleeping')

print('Ex2-1 : ', wi)   # repr 때문에.
print('Ex2-2 : ', next(wi))
print('Ex2-3 : ', next(wi))
print('Ex2-4 : ', next(wi))
print('Ex2-5 : ', next(wi))
print('Ex2-6 : ', next(wi))
print('Ex2-7 : ', next(wi))
print('Ex2-8 : ', next(wi))
# print('Ex2-9 : ', next(wi))
# 다음에 나올 글자를 커서만 가르키고 next()를 실행할 때 반환해준다 -> 즉, Generator 의 일을 한다. 한 글자 하나하나를 필요할 떄 호출하여 반환해주는 것

print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가 될 경우 메모리 사용량이 증가하기 때문에 이를 제너레이터로 완화한다.
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3. 딕셔너리, 리스트 등 한 번 호출할 때 마다 하나의 값만 리턴. -> 아주 작은 메모리의 양을 필요로 한다.


class WordSplitGenerator():
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word  # 제네레이터
        return

    # 매직 메소드
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wg = WordSplitGenerator('Who says the nights are for sleeping')

wt = iter(wg)   # next 가 구현되어 있지 않기 때문에 iterable 하게 만들어준다.
print('Ex3-1 : ', wt)   # repr 때문에.
print('Ex3-2 : ', next(wt))
print('Ex3-3 : ', next(wt))
print('Ex3-4 : ', next(wt))
print('Ex3-5 : ', next(wt))
print('Ex3-6 : ', next(wt))
print('Ex3-7 : ', next(wt))
print('Ex3-8 : ', next(wt))
# print('Ex3-9 : ', next(wt))


# Generator 예제1

def generator_ex1():
    print('start!')
    yield 'AAA'
    print('continue')
    yield 'BBB'
    print('end')


temp = iter(generator_ex1())

# print('Ex4-1 : ', next(temp))
# print('Ex4-2 : ', next(temp))
# print('Ex4-3 : ', next(temp))

for v in generator_ex1():
    # print('Ex4-4 : ', v)
    # 에러를 알아서 잡고 탈출한다.
    pass

print()

# Generator 예제2

temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())    # 지능형 제네레이터

print('Ex5-1 : ', temp2)    # ['AAAAAAAAA', 'BBBBBBBBB'] 반환
# Generator 객체가 반환. next() 메소드를 호출하기 전 까지는 값을 생성하지 않는다.
print('Ex5-2 : ', temp3)

for i in temp2:
    print('Ex5-3 : ', i)

for i in temp3:
    print('Ex5-4 : ', i)

print()

# Generator 예제3(자주 사용하는 함수)

# import itertools

gen1 = itertools.count(1, 2.5)

print('Ex6-1 : ', next(gen1))
print('Ex6-2 : ', next(gen1))
print('Ex6-3 : ', next(gen1))
print('Ex6-4 : ', next(gen1))
# ... 무한히 호출 가능 but 메모리를 잡아먹지 않는다.


# 조건
gen2 = itertools.takewhile(lambda n: n < 100, itertools.count(1, 2.5))

for v in gen2:
    print('Ex6-5 : ', v)

print()


# 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print('Ex6-6 : ', v)

print()


# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 11)])

for v in gen4:
    print('Ex6-7 : ', v)

print()


# 연결1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))

print('Ex6-8 : ', list(gen5))

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))

print('Ex6-9 : ', list(gen6))


# 개별
gen7 = itertools.product('ABCDE')

print('Ex6-10 : ', list(gen7))

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)

print('Ex6-11 : ', list(gen8))


# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')

# print('Ex6-12 : ', list(gen9))

for chr, group in gen9:
    print('Ex6-12 : ', chr, ' : ', list(group))

print()
