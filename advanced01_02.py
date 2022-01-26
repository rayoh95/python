# 클래스 변수, 인스턴스 변수

# 클래스 선언
class Student():
    """
    Student Class
    Authod : OSH
    Date : 2021.01.27
    """

    # 클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        # Student 객체가 생성될 때 마다 student_count 가 증가한다.
        Student.student_count += 1

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))   # 고유의 id 값(reference 값) 출력
        print('Student Detail Info : {} {} {}'.format(
            self._mane, self._email, self._details))

    # 오버라이딩
    def __del__(self):
        Student.student_count -= 1


# Self 의미
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 53, 'score2': 44})
studt2 = Student(
    'Song', 2, 3, {'gender': 'Female', 'score1': 69, 'score2': 54}, 'stu2@naver.com')

print(id(studt1))
print(id(studt2))
# 다른 숫자가 의미하는 것은 다른 객체라는 의미이다.(주소값)

# ID 확인
print(studt1 == studt2)
# 인스턴스 변수값 확인
print(studt1._name == studt2._name)
print(studt1 is studt2)

# dir & __dict__ 확인
print(dir(studt1))
print(dir(studt2))
print(studt1.__dict__)
print(studt2.__dict__)

# Doctring
print(Student.__doc__)

# 실행
studt1.detail_info()
studt2.detail_info()

# 에러
# Student.detail_info()
# 에러문: 필요한 인자인 self 가 없다.

Student.detail_info(studt1)
# 출력 가능, studt1 이 self 역할을 한다.

# 비교
print(studt2.__class__)  # 부모를 알려준다.
print(studt2.__class__)  # 위와 똑같은 값을 가진다.
print(id(studt1.__class__) == id(studt2.__class__))  # True

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장하지 않는다.) -> 캡슐화를 권장
print(studt1._name, studt2._name)
print(studt1._email, studt2._email)

# 클래스 변수
# 접근
print(studt1.student_count)  # 누구나 접근 가능
print(studt2.student_count)
print(Student.student_count)

# 클래스 변수가 공유되었는지 확인
print(Student.__dict__)
print(studt1.__dict__)  # 안에 student_count 없다.
# 인스턴스 네임스페이스 없으면 상위에서 알아서 검색
# 즉, 동일한 이름으로 변수 생성 가능하다.(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))

del studt1

print(studt2.student_count)
print(Student.student_count)
