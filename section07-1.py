# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스 , 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 떄 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별로도 존재. 인스턴스 생성 후 사용한다.

# 선언
# class 클래스명:
#     함수

class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

user1 = UserInfo("Kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)


# self 의 이해
class SelfTest:

    #클래스 메소드
    def function1():
        print('function1 called!')  
    #인스턴스 메소드
    def function2(self):
        print(id(self))
        print('function2 called!')
    
self_test = SelfTest()
self_test.function1()   #에러가 난다. 
SelfTest.function1()    #function1 은 클래스를 통해서만 호출 가능. 클래스 메소드인 것이다.
self_test.function2()   #호출 가능

print(id(self_test))
SelfTest.function2(self_test)


# 클래스 변수, 인스턴스 변수
class WareHouse:
    #클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(slef):
        WareHouse.stock_num -=1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)   #클래스 네임스페이스, 클래스 변수(공유)

print(user1.stock_num)  #자기 네임 스페이스에 없으면 클래스의 네임 스페이스로 가서 찾는다. 클래스에도 없으면 에러

del user1


