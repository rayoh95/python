# 객체 지향 프그밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 일반적인 코딩

# 학생1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender': 'Male'},
    {'score1': 95},
    {'score2': 88}
]

# 학생2
student_name_2 = 'Park'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender': 'Female'},
    {'score1': 90},
    {'score2': 69}
]

# 학생3
student_name_3 = 'Lee'
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = [
    {'gender': 'Male'},
    {'score1': 99},
    {'score2': 100}
]

# 리스트 구조
# 관리하기 불편
# 데이터의 정확한 위치(인덱스)매핑하여 사용해야 한다.
student_names_list = ['Kim', 'Park', 'Lee']
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 4]
student_details_list = [
    {'gender': 'Male', 'score1': 95, 'score2': 88},
    {'gender': 'Female', 'score1': 90, 'score2': 69},
    {'gender': 'Male', 'score1': 99, 'score2': 100}
]

# 학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

print('\n')

# 딕셔너리 구조
# 코드 반복 시족, 중첩 문제
students_dicts = [
    {'student_name': 'Kim', 'student_number': 1, 'student_grade': 1,
        'student_detail': {'gender': 'Male', 'score1': 95, 'score2': 88}},
    {'student_name': 'Park', 'student_number': 2, 'student_grade': 3,
        'student_detail': {'gender': 'Male', 'score1': 90, 'score2': 69}},
    {'student_name': 'Lee', 'student_number': 3, 'student_grade': 4,
        'student_detail': {'gender': 'Male', 'score1': 99, 'score2': 100}}
]

del students_dicts[1]
print(students_dicts)
print('\n')


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Student():
    # 생성자
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str : {}'.format(self._name)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._name, self._number)


student1 = Student('Kim', 1, 1, {'gender': 'Male', 'score1': 95, 'score2': 88})

student2 = Student(
    'Park', 2, 2, {'gender': 'Female', 'score1': 90, 'score2': 69})

student3 = Student(
    'Lee', 3, 4, {'gender': 'Male', 'score1': 99, 'score2': 100})

print(student1.__dict__)
# 학생의 속성값이 모두 포함된 네임 스페이스를 출력한다.
print(student2.__dict)
print(student3.__dict)

# 리스트 선언
students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print()

print(students_list)
# 각 객체들의 주소값들이 출력된다.

# 반복(__str__)
for x in students_list:
    print(x)
    # kim, lee, park 가 출력된다. 그 이유는 student 객체의 __str__(self) 함수 때문(오버라이딩)
    # str 메소드가 repr 메소드보다 우서순위가 높다.

    print(repr(x))
    # repr 메소드가 호출
