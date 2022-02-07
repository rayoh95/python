# yeild
# 코루틴(Coroutine)

# yield : 메인루틴 <-> 서브 루틴 (통신)
# 코루틴 제어, 코루틴 상태, 양방향 값 전송
# yield from

# 서브루틴 : 메인 루틴에서 -> 리턴에 의해 호출 부분으로 돌아와 다시 프로세스 진행
# 코루틴 : 루틴 실행 중 멈춤 가능 -> 특정 위치로 돌아갔다가 -> 다시 원래 위치로 돌아와 수행 -> 동시성 프로그램을 가능하게 해준다.
# 코루틴 : 코루틴은 스케쥴링 오버헤드가 매우 적다. -> 메모리 할당을 최소화하여 시간이 적게 걸린다.
# 쓰레드 : 운영체제에서 지원해주는 것이다. 멀티쓰레드는 복잡하다. 공유도는 자원에 대한 교착 상태가 발생할 가능성이 있기 때문이다.(주의깊게 코리도어 해야한다.), 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가

from functools import wraps
from inspect import getgeneratorstate
from optparse import TitledHelpFormatter

# 코루틴 예제1


def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 제네레이터 선언


c1 = coroutine1()

print('Ex1-1 : ', c1, type(c1))
# type 이 generator 이다.

# yield 실행 전까지 진행
# next(c1)

# 기본으로 None 전달
# next(c1)  두 번째 next 이므로 오류가 난다 : StopIteration

# 값 전송
# c1.send(100)

# 잘못된 사용

c2 = coroutine1()

# c2.send(100)
# generator 을 실행한 다음 값을 보내야한다. next() 로 호출한 수 yield 에서 멈추어놔야 가능하다.

# 코루틴 예제2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태


def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x     # y 는 메인 루틴이 코루틴한테 send 로 보내주는 값, x 는 우리가 메인 루틴한테 전달하는 값
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


c3 = coroutine2(10)

# from inspect import getgeneratorstate

print('Ex1-2 : ', getgeneratorstate(c3))    # GEN_CREATED
print(next(c3))  # coroutine started : 10    10

print('Ex1-3 : ', getgeneratorstate(c3))    # GEN_SUSPENDED

print(c3.send(15))  # coroutine received : 15   25

# print(c3.send(20))  # coroutine received : 20   StopIteration   -> 예외

print()

# 데코레이터 패턴

# from functools import wraps


def coroutine(func):
    '''Decorator run until yield'''
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def sumer():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term


su = sumer()

print('Ex2-1 : ', su.send(100))
print('Ex2-2 : ', su.send(40))
print('Ex2-3 : ', su.send(60))
# next() 호출을 생략했다.


# 코루틴 예제3(예외처리)

class SampleException(Exception):
    '''설명에 사용할 예외 유형(껍데기)'''


def coroutine_except():
    print('>>> coroutine started.')
    try:
        while True:
            try:
                x = yield
            except SampleException:
                print('-> SampleException handled. Continuing..')
            else:   # try 문이 무사히 실행되면 else 문이 실행된다.
                print('>>> coroutine received : {}'.format(x))
    finally:
        print('-> coroutine end')


exe_co = coroutine_except()

print('Ex3-1 : ', next(exe_co))
print('Ex3-2 : ', exe_co.send(10))
print('Ex3-3 : ', exe_co.send(100))
print('Ex3-4 : ', exe_co.throw(SampleException))
print('Ex3-5 : ', exe_co.send(1000))
print('Ex3-6 : ', exe_co.close())   # GEN_CLOSED
# print('Ex3-2 : ', exe_co.send(10))  # 에러(StopIteration)

print()

# 코루틴 예제4(return)


def averager_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total / cnt
    return 'Average : {}'.format(avg)


avger2 = averager_re()

next(avger2)

avger2.send(10)
avger2.send(30)
avger2.send(50)

try:
    avger2.send(None)
except StopIteration as e:
    print('Ex4-1 : ', e.value)
# Coroutine 이 반환하는 값은 에러문에 담겨있다.


# 코루틴 예제5(yield from)
# StopIteration 자동 처리(3.7 -> await)
# 중첩 코루틴 처리

def gen1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


t1 = gen1()

print('Ex5-1 : ', next(t1))
print('Ex5-2 : ', next(t1))
print('Ex5-3 : ', next(t1))
print('Ex5-4 : ', next(t1))
print('Ex5-5 : ', next(t1))
# print('Ex5-6 : ', next(t1))   # StopIteration

t2 = gen1()

print('Ex5-7 : ', list(t2))

print()


def gen2():
    yield from 'AB'
    yield from range(1, 4)
# gen1 과 같은 의미. yield from 이 알아서 제어해준다.


t3 = gen2()

print('Ex6-1 : ', next(t3))
print('Ex6-2 : ', next(t3))
print('Ex6-3 : ', next(t3))
print('Ex6-4 : ', next(t3))
print('Ex6-5 : ', next(t3))
# print('Ex6-6 : ', next(t3))   # StopIteration


t4 = gen2()

print('Ex6-7 : ', list(t4))

print()


def gen3_sub():
    print('Sub coroutine.')
    x = yield 10
    print('Recv : ', str(x))
    x = yield 100
    print('Recv : ', str(x))


def gen4_main():
    yield from gen3_sub()
# gen4_main() 은 코루틴의 중제자 역할을 한다. -> 코루틴 끼리의 통신


t5 = gen4_main()

print('Ex7-1 : ', next(t5))
print('Ex7-2 : ', t5.send(7))
print('Ex7-3 : ', t5.send(77))  # StopIteration 발생
