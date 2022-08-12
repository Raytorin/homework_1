class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, student, course, grade):
        if isinstance(lector, Lector) and course in lector.courses_attached and isinstance(student, Student) and course in student.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

 
best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python']

best_student_2 = Student('Tessay', 'Root', 'male')
best_student_2.courses_in_progress += ['Git']

cool_lector_1 = Lector('Some', 'Buddy')
cool_lector_1.courses_attached += ['Python']

cool_lector_2 = Lector('Oncet', 'Oldme')
cool_lector_2.courses_attached += ['Git']

cool_reviewer_1 = Reviewer('Thew', 'Orld')
cool_reviewer_1.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Gone', 'Rolme')
cool_reviewer_2.courses_attached += ['Git']

cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)
cool_reviewer_2.rate_hw(best_student_2, 'Git', 8)

best_student_1.rate_lector(cool_lector_1, best_student_1, 'Python', 9)
best_student_2.rate_lector(cool_lector_2, best_student_2, 'Git', 10)
 
print(f'Студент 1 - {best_student_1.grades}')
print(f'Студент 2 - {best_student_2.grades}')

print(f'Лектор 1 - {cool_lector_1.grades}')
print(f'Лектор 2 - {cool_lector_2.grades}')