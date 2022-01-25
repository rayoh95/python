# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1 (클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)
print("ex2 : ", Fibonacci('Title').title)


# 사용3 (클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

print("ex3 : ", Fibonacci.fib2(1600))
print("ex3 : ", Fibonacci().title)
print("ex3 : ", Fibonacci('Title').title)


# 사용4 (함수)
import pkg.circulations as cal

print("ex4 : ", cal.add(10, 100))
print("ex4 : ", cal.mul(10, 100))


# 사용5 (함수)
from pkg.circulations import div as d

print("ex 5 : ", int(d(100, 10)))


# 사용6
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))

