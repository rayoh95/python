# 상속, 다중상속

# 부모클래스(슈퍼클래스) 및 자식클래스(서브클래스) -> 모든 속성, 메소드 사용 가능
# 상속을 사용하는 이유: 코드를 재사용 가능하고, 중복을 최소화한다. 가독성 관련 장점

class Car:
    """"Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car class "Show MEthod!"'
    
class BmwCar(Car):
    """"Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    def show_model(self):
        return "Your Car name : %s" % self.car_name

class BenzCar(Car):
    """"Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    def show_model(self):
        return "Your Car name : %s" % self.car_name

    def show(self):
        print(super().show())   #super 라는 예약어를 통해 부모의 변수나 생성자 등 접근 가능
        return 'Car Info : %s %s %s' %(self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('520d', 'sadan', 'red')

print(model1.color) # 부모에서 가져온 값
print(model1.type)  
print(model1.car_name)  # 자식의 값
print(model1.show())    # 부모의 메소드
print(model1.show_model())  # 자식의 메소드
print(model1.__dict__)


# Method Overriding(오버라이딩)
model2 = BenzCar("220d", 'suv', "black")
print(model2.show())    # 자식의 메소드...오버라이딩


# Parent Method Call 부모 메소드 바로 부르기
model3 = BenzCar("350s" , 'sedan', "silver")
print(model3.show())    #오버라이딩 된 자식 메소드

# 상속의 관계가 깊을 때, depth 가 깊을 떄
# Inheritance Info 상속의 정보를 라스트 타입으로 보여주는 메소드가 존재
print(BmwCar.mro())
print(BenzCar.mro())


# 다중 상속

class X():
    
    pass

class Y():

    pass

class Z():

    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
print(A.mro())
    