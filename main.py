# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.av_grade = "0"

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            print(f"Поставить оценку по курсу {course} {self.name} {self.surname} не может.")
    def average_grade(self):
        list= []
        sum = 0
        for grade in self.grades.values():
            list += grade
        k = len(list)
        for i in range(k):
            sum += int(list[i])
        av_rate = round((sum/k), 2)
        self.av_grade = av_rate
    def __str__(self):
        rep = "Имя: " + self.name + "\n"
        rep += "Фамилия: "+ self.surname+"\n"
        rep += "Средняя оценка за домашние задания: " + str(self.av_grade) + "\n"
        rep += "Курсы в процессе изучения: " + ", ".join(self.courses_in_progress) + "\n"
        rep += "Завершённые курсы: " + ", ".join( self.finished_courses)
        return rep
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student")
            return
        return self.av_grade < other.av_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        rep = "Имя: " + self.name + "\n"
        rep += "Фамилия: " + self.surname + "\n"
        return rep


# Создаём экземпляр класса Student
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.grades['Git'] = [10, 10, 10, 9, 10]
best_student.grades['Python'] = [10, 10]


best_student1 = Student('Joney', 'Deb', 'your_gender')
best_student1.finished_courses += ['Git']
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['VB']
best_student1.grades['Git'] = [10, 7, 10, 9, 10]
best_student1.grades['Python'] = [10, 5]

# Создаём экземпляр класса Mentor
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
#print(cool_mentor.courses_attached)


# Наследование
class Lecturer(Mentor):
    # Добавление атрибута
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.rates = {}
        self.av_r = 0
    def average_rate(self):
        list = []
        sum = 0
        for rate in self.rates.values():
            list += rate
        k = len(list)
        for i in range(k):
            sum += int(list[i])
        av_rate = round(sum/k, 2)
        self.av_r = av_rate
    def __str__(self):
        rep = "Имя: " + self.name +"\n"
        rep += "Фамилия: " + self.surname+"\n"
        rep += "Средняя оценка за лекции: " + str(self.av_r)
        return rep
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer")
            return
        return self.av_r < other.av_r

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


cool_reviewer = Reviewer('Some2', 'Buddy2')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['VB']
#print(cool_reviewer.courses_attached)
cool_reviewer1 = Reviewer('Ivan', 'Prigogin')
cool_reviewer1.courses_attached += ['C++']
#print(cool_reviewer1.courses_attached)
# Выставление оценки студенту Reviewer
cool_reviewer.rate_hw(best_student, 'Python', '9')
#print(best_student.grades)
cool_lecturer = Lecturer("Clever", "Human")
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['C++']
cool_lecturer1 = Lecturer("Ivan", "Ivanov")
cool_lecturer1.courses_attached += ['VB']
cool_lecturer1.courses_attached += ['Python']
# Выставление оценки лектору студентом за лекции по курсам
best_student.rate_lecturer(cool_lecturer, 'Python', '7')
best_student.rate_lecturer(cool_lecturer, 'C++', '8')
best_student.rate_lecturer(cool_lecturer, 'C++', '6')
best_student.rate_lecturer(cool_lecturer1, 'VB', '9')
best_student1.rate_lecturer(cool_lecturer1, 'VB', '5')
best_student1.rate_lecturer(cool_lecturer1, 'C++', '10')
best_student1.rate_lecturer(cool_lecturer1, 'Python', '10')
cool_lecturer.average_rate()
cool_lecturer1.average_rate()
best_student.average_grade()
best_student1.average_grade()
print(cool_lecturer.rates)
print(cool_lecturer.av_r)
print(cool_lecturer1.rates)
print(cool_lecturer1.av_r)
# Вывожу на печать проверяющего
# print(cool_reviewer)
# print(cool_reviewer1)
print(cool_lecturer)
print(cool_lecturer1)
print(best_student)
print(best_student1)
# Сравниваем студентов по средней оценке
print(best_student1<best_student)
# Сравниваем лекторов по среднему рейтингу
print(cool_lecturer1 < cool_lecturer)

print(best_student.grades)
print(best_student1.grades)
# Функция поиска средней оценки студентов в рамках одного курса
def average_rating_stud_course(st_list, course):
    grade_list = []
    sum=0
    for st in st_list:
        grade_list += st.grades[course]
    k = len(grade_list)
    for i in range(k):
        sum += int(grade_list[i])
    av_grade = round(sum / k, 2)
    print(f'Средняя оценка среди студентов по курсу {course}: {av_grade}')
average_rating_stud_course([best_student, best_student1], 'Python')

print(cool_lecturer.rates)
print(cool_lecturer1.rates)
# Функция поиска средней оценки лекторов в рамках одного курса
def average_rating_lect_course(lec_list, course):
    grade_list=[]
    sum=0
    for lec in lec_list:
        grade_list += lec.rates[course]
    k = len(grade_list)
    for i in range(k):
        sum += int(grade_list[i])
    av_grade = round(sum / k, 2)
    print(f'Средняя оценка среди лекторов по курсу {course}: {av_grade}')
average_rating_lect_course([cool_lecturer, cool_lecturer1], 'Python')