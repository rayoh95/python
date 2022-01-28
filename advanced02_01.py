# 데이터 모델(Data Model)
# 참조 : http://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value 를 갖고 있다.
# 파이썬 -> 일관성

# 일반적인 튜플 사용

from collections import namedtuple
from math import sqrt
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)


line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

print('Ex1-1 : ', line_leng1)


# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

# 두 점 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

line_leng2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

print('Ex1-2 : ', line_leng2)
print('Ex1-3 : ', line_leng1 == line_leng2)  # True 출력


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)  # Default=False

# 출력
print('Ex2-1 : ', Point1, Point2, Point3, Point4)


# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성

p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)    # 딕셔너리 언패킹하여 자동으로 바인딩해준다.

print('Ex2-2 : ', p1, p2, p3, p4, p5)
# p4 의 중복된 x 와 예약어 class 의 사용은 알아서 다른 변수명을 선언해준다.
print(p4._2, p4._3)

# 사용
print('Ex3-1 : ', p1[0] + p2[1])    # 인덱스 활용 가능
print('Ex3-1 : ', p1.x + p2.y)  # 클래스 변수 접근 방식

# Unpacking
x, y = p3

print('Ex3-3', x + y)

# Rename 테스트
print('Ex3-4', p4)

print()

# 네임드 튜플 메소드

temp = [52, 38]  # 데이터를 담을 수 있는 sequence 형, literable

# _make() : 새로운 객체 생성
p6 = Point1._make(temp)

print('Ex4-1 : ', p6)

# _fields : 필드 네임 확인
print('Ex4-2 : ', p1._fields, p2._fields, p3._fields, p4._fields)

# _asdict() : OrderedDict 반환
print('Ex4-3 : ', p1._asdict(), p6._asdict())

# _replace() : 수정된 '새로운' 객체를 반환 (id 값이 바뀐다.)
print('Ex4-4 : ', p2._replace(y=100))

print()

# 실 사용 실습
# 학생 전체 그룹 생성
# 반 20명, 4개의 반 -> (A,B,C,D) 번호

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]    # List Comprehension
ranks = 'A B C D'.split()

print(ranks, numbers)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print('Ex5-1 : ', students, len(students))
print('Ex5-2 : ', students[4].rank)


# 가독성 안좋은 경우
print()
students2 = [Classes(rank, number)
             for rank in 'A B X D'.split()
             for number in [str(n)
                            for n in range(1, 21)]]

print('Ex6-1 : ', students2, len(students2))
print('Ex6-2 : ', students2[4].rank)

# 출력
for s in students:
    print('Ex7-1 : ', s)
