# 예외처리

# 문법적으로는 에러가 없지만, 코드 실행(런타임)프로세스에서 방생하는 예외 처리도 중요
# linter : 코드 스타일을 알려주며 문법을 체크한다. -> 문법적인 에러를 잡기 쉽다.


# SyntaxError : 잘못된 문법

# print('Test)
# if True
#    pass

# NameError : 참조변수 없음

a = 10
b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
# print(x[3])

# keyError

dic = {'name' : 'kim', 'age' : 33, 'city' : 'seoul'}

# print(dic['hobby'])
print(dic.get('hobby'))


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
print(time.time())
# print(time.month())

# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]
#x.remove(10)
#x.index(10)

# FileNotFoundError

# f = open('test.txt', 'r')

# TypeEror

x = [1,2]
y = (1,2)
z = 'test'

# print(x + y)
# print(x + z)
print(x + list(y))  #형변환

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행되는 구문


#예제 1
name = ['kim', 'lee', 'park']

try:
    z = 'kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('OK! else!')


#예제 3
name = ['kim', 'lee', 'park']

try:
    z = 'jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occurred ValueError!')
else:
    print('OK! else!')
finally:
    print('fionally ok!')


# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('Ok Finally!!!')


# 예제 5
name = ['kim', 'lee', 'park']

try:
    z = 'jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as l:
    print(l)
    print('Not found it! - Occurred ValueError!')
except IndexError:
    print('Not found it! - Occurred IndexError!')
except Exception:
    print('Not found it! - Occurred Error!')
else:
    print('OK! else!')
finally:
    print('fionally ok!')


# 예제 6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a == "Kim":
        print('Ok 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('Ok!')