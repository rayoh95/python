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
