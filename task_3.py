class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lector) and course in lector.courses_attached and isinstance(self, Student) and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def _middle_grades_student(self):
        final_sum_grades_student = 0
        count_numbers_student = 0
        for numbers_student in self.grades.values():
            for sum_grades_student in numbers_student:
                final_sum_grades_student += sum_grades_student
                count_numbers_student += 1
        self.final_grade_student = final_sum_grades_student // count_numbers_student
        return self.final_grade_student

    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            if self._middle_grades_student() > other._middle_grades_student():
                return f'{self.name} {self.surname} имеет большую оценку ({self._middle_grades_student()})'
            else: 
                return f'{other.name} {other.surname} имеет большую оценку ({other._middle_grades_student()})'
        else:
            return 'Ошибка'

    def __str__(self):
        some_student_1 = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._middle_grades_student()} \n'
        some_student_2 = f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)} \n'
        return some_student_1 + some_student_2
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _middle_grades_lector(self):
        final_sum_grades = 0
        count_numbers = 0
        for numbers in self.grades.values():
            for sum_grades in numbers:
                final_sum_grades += sum_grades
                count_numbers += 1
        self.final_grade = final_sum_grades // count_numbers
        return self.final_grade
    
    def __lt__(self, other):
        if isinstance(self, Lector) and isinstance(other, Lector):
            if self._middle_grades_lector() > other._middle_grades_lector():
                return f'{self.name} {self.surname} имеет большую оценку ({self._middle_grades_lector()})'
            else: 
                return f'{other.name} {other.surname} имеет большую оценку ({other._middle_grades_lector()})'
        else:
            return 'Ошибка'

    def __str__(self):
        some_lector = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._middle_grades_lector()} \n'
        return some_lector


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def __str__(self):
        some_reviewer = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        return some_reviewer
 
best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python']

best_student_2 = Student('Tessay', 'Root', 'male')
best_student_2.courses_in_progress += ['Git']
best_student_2.finished_courses += ['Python']

best_student_3 = Student('Te', 'Ro', 'male')
best_student_3.courses_in_progress += ['Python']

cool_lector_1 = Lector('Some', 'Buddy')
cool_lector_1.courses_attached += ['Python']

cool_lector_2 = Lector('Oncet', 'Oldme')
cool_lector_2.courses_attached += ['Git']

cool_reviewer_1 = Reviewer('Thew', 'Orld')
cool_reviewer_1.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Gone', 'Rolme')
cool_reviewer_2.courses_attached += ['Git']

cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)
cool_reviewer_1.rate_hw(best_student_3, 'Python', 7)
cool_reviewer_2.rate_hw(best_student_2, 'Git', 8)
cool_reviewer_2.rate_hw(best_student_2, 'Git', 10)

best_student_1.rate_lector(cool_lector_1, 'Python', 9)
best_student_2.rate_lector(cool_lector_2, 'Git', 10)
best_student_3.rate_lector(cool_lector_1, 'Python', 5)
 
print(f'Студент 1 - {best_student_1.grades}')
print(f'Студент 2 - {best_student_2.grades}')

print(f'Лектор 1 - {cool_lector_1.grades}')
print(f'Лектор 2 - {cool_lector_2.grades}')

print(cool_reviewer_1)

print(cool_lector_1)

print(best_student_2)

print(cool_lector_1.__lt__(cool_lector_2))

print(best_student_3.__lt__(best_student_2))