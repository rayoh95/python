# 사용자 정의 함수
# 함수 선언 위치 중요

def hello(world):
    print("Hello ", world)

hello("Python!")
hello(7777)

def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Phython!!!!")
print(str)

# 다중 리턴
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))


# *args, *kwargs

def args_func(*args):
    print(args)

args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')
# 튜플 형태

def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1='kim', name2='park', name3='lee')
# 딕셔너리 형태

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)


# 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)


# lambda 예제
# 람다식: 메모리 절약. 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10   # 선언하는 것 만으로도 메모리를 할당한다. 파이썬 내 interpreter 에서 일어나는 일
print(var_func) 

# 람다식
lambda_mul_10 = lambda num : num * 10

lambda_mul_10(10)

def func_final(x, y, func):
    print( x * y * func(10))

func_final(10,10,lambda_mul_10)

func_final(10, 10, lambda x: x * 1000)
