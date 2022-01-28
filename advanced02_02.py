# Special Method(Magic Method)
# 참조1 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 참조2 : https://www.tutorialsteacher.com/python/magic-methods-in-python

# 매직메소드 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 매직메소드 기초 설명

# 기본형

print(int)

# 모든 속성 및 메소드 출력
print(dir(int))
print()

n = 100

# 사용
print('Ex1-1 : ', n + 200)
print('Ex1-2 : ', n.__add__(200))
print('Ex1-3 : ', n.__doc__)
print('Ex1-4 : ', n.__bool__(), bool(n))
print('Ex1-5 : ', n * 100, n.__mul__(100))

print()

# 클래스 예제1


class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    # str 메소드를 overroding 해서 작성하는 것이 좋다.
    def __str__(self):
        return 'Student Class Info : {} , {}'.format(self._name, self._height)

    def __ge__(self, x):
        print('Called. >> __ge__ Method.')
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x):
        print('Called. >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called. >> __sub__ Method.')
        return self._height - x._height


# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)

print(s1._height > s2._height)

# 매직메소드 출력
print('Ex2-1 : ', s1 >= s2)
print('Ex2-2 : ', s1 <= s2)
print('Ex2-3 : ', s1 - s2)
print('Ex2-4 : ', s2 - s1)
print('Ex2-5 : ', s1)
print('Ex2-6 : ', s2)

print()

# 클래스 예제

# 벡터(Vector)


class Vector(object):
    def __init__(self, *args):
        """
        Create a vector, example : v = Vector(1,2)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Returns the vector information'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Returns the vector addition of self and other's'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

# 메직메소드 출력
print('Ex3-1 : ', Vector.__init__.__doc__)
print('Ex3-2 : ', Vector.__repr__.__doc__)
print('Ex3-3 : ', Vector.__add__.__doc__)
print('Ex3-4 : ', v1, v2, v3)
print('Ex3-5 : ', v1 + v2)
print('Ex3-6 : ', v1 * 4)
print('Ex3-7 : ', v2 * 10)
print('Ex3-8 : ', bool(v1), bool(v2))
print('Ex3-9 : ', bool(v3))

print()
