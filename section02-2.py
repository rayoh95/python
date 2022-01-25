import this
import sys

print(sys.stdin.encoding)
print(sys.stdout.encoding)

def greeting():
    print("Nice to meet you!")

greeting()

#클래스

class Cookie:
    pass

#객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))