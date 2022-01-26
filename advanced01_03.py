# 클래스 메소드, 인스턴스 메소드, 스테틱 메소드

# 기본 인스턴스 메소드

class Student(object):
    """
    Student Class
    Author : OSH
    Date : 2021.01.27
    Description : Class, Static, Instance Method
    """
    # 위 주석은 doctring 으로 확인 가능

    # Class Variable
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id   # self.id = id 로 해도 괜찮음
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        # self 를 인자로 받아 호출하는 method 가 instance method 이다.
        return '{} {}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    # Instance Method
    def get_fee(self):
        return 'BeFore Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    def get_fee_culc(self):
        return 'After Tuition -> Id : {}, fee : {}'.format(self._id, (self._tuition * Student.tuition_per))

    def __str__(self):
        return 'Student Info -> name : {} grade : {} email : {}'.format(self.full_name(), self._grade, self._email)

    # Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please Enter larger than 1')
            return
        cls.tuition_per = per
        print('Succed! tuition increased!')

    # Class Method
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition, gpa)

    # Static Method
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa > 4.3:
            return '{} is a scholarship recipient.'.format(inst.full_name())
        return 'Sorry. Not a scholarship recipient.'


student_1 = Student(1, 'Ahn', 'Jaehyun', 'student1@naver.com', '4', 400, 3.8)
student_2 = Student(2, 'Ahn', 'Yeonhee', 'student2@daum.net', '1', 350, 4.3)

print(student_1.__dict__)
print(student_2.__dict__)
# 기본 정보
print(student_1)
print(student_2)

# 전체 정보
print(student_1.detail_info())
print(student_2.detail_info())

# 학비 정보(인상 전)
print(student_1.get_fee())
print(student_2.get_fee())

# 학비 인상(클래스 메소드 미사용)
Student.tuition_per = 1.2   # 직접 접근은 좋지 않다.
Student.raise_fee(1.2)

# 학비 정보(인상 후)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())


# 클래스 메소드로 인스턴스 생성하기 (메소드 이름을 통해 직관적으로 무슨 기능을 하는 함수인지 알 수 있다.)
student_3 = Student.student_const(
    3, 'Song', 'Minji', 'Student3@gmail.com', '2', 380, 4.5)
student_4 = Student.student_const(
    3, 'Jo', 'Suk', 'Student4@hotmail.com', '4', 400, 3.1)

# 전체 정보
print(student_3.detail_info())
print(student_4.detail_info())

# 학생 학비 변경 확인
print(student_3._tuition)
print(student_4._tuition)


# 장학금 혜택 여부(스테틱 메소드 미사용)
def is_scholarship(inst):
    if inst._gpa > 4.3:
        return '{} is a scholarship recipient.'.format(inst.full_name())
    return 'Sorry. Not a scholarship recipient.'


print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

# 장학금 혜택 여부(스테틱 메소드 사용)
print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print(student_1.is_scholarship_st(student_1))
print(student_2.is_scholarship_st(student_2))
print(student_3.is_scholarship_st(student_3))
print(student_4.is_scholarship_st(student_4))
# 접근하는 방법이 매우 유연하다. class method 로도, instance method 로도 호출 가능
