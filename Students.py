
class Student:
    persons_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.persons_list.append([name, surname])
    
    

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lector) and course in lector.courses_attached and course in self.courses_in_progress:
            if int(grade)> 10 or int(grade) < 0:
                print('Введите число от 0 до 10')
                return
            elif course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
            
        
    def average_grade(self):
        amount_hw = 0
        sum_of_grades = 0
        for course in self.grades:
            for grade in self.grades[course]:
                sum_of_grades += grade
                amount_hw += 1
        if amount_hw == 0:
            av_grade = 'Недостаточно оценок'       
        else:
            av_grade = float("{0:.1f}".format(sum_of_grades / amount_hw))
        return av_grade

   
    def __eq__(self, other_student):
        if isinstance(other_student, Student):
            
            if self.average_grade() == other_student.average_grade():
                return 'Оба хороши'
            else:
                return 'Стиль обучения отличается'
        else:
            return 'Сравнение неуместно'
        
   
    def __str__(self):
        fin_courses = ''.join(self.finished_courses)
        cont_courses = ''.join(self.courses_in_progress)
        average = self.average_grade()
        if cont_courses == '':
            cont_courses = 'Нет'
        elif fin_courses == '':
            fin_courses = 'Нет'
              
        visit_card = f'Студент\nИмя = {self.name} \
                    \nФамилия = {self.surname}\
                    \nСредняя оценка за домашние задания = {average}\
                    \nИзучаемые курсы = {fin_courses}\
                    \nЗавершенные курсы = {cont_courses}'
        return visit_card


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
            

class Lector(Mentor):
    persons_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)    
        self.courses_attached = []
        self.grades = {}
        Lector.persons_list.append([name, surname])
    
    def __str__(self):
        
        average = Student.average_grade(self)
                      
        visit_card = f'Лектор\nИмя = {self.name} \
                    \nФамилия = {self.surname}\
                    \nСредняя оценка за лекции = {average}'
        return visit_card

    def __eq__(self, other_lector):
        if isinstance(other_lector, Lector):
            if Student.average_grade(self) == Student.average_grade(other_lector):
                return 'Лекторы равноценны'
            else:
                return 'Стиль преподавания отличается'
        else:
            return 'Сравнение неуместно'
        

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if type(grade) != int or 0 > grade <10:
                return 'Введите число от 0 до 10'
            elif course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        
        visit_card = f'Аспирант\nИмя = {self.name} \
                    \nФамилия = {self.surname}'
        return visit_card


def hw_for_course(course):
    grades = 0
    amount_hw = 0
    if 

   
    return ("Такого лектора или студента в базе нет")
    





best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']

worst_student = Student('Mike', 'Oxlong', 'helicopter')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['GIT']

cool_mentor = Lector('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['GIT']

lector1 = Lector('Ганнибал','Лектор')
lector1.courses_attached += ['Python']
lector1.courses_attached += ['GIT']

even_cooler_mentor = Reviewer('Once','Told me')
even_cooler_mentor.courses_attached += ['Python']
even_cooler_mentor.courses_attached += ['GIT']


even_cooler_mentor.rate_hw(best_student, 'Python', 7)
even_cooler_mentor.rate_hw(worst_student, 'Python', 2)
even_cooler_mentor.rate_hw(best_student, 'GIT', 10)
best_student.rate_lector(cool_mentor, 'Python', 10)
best_student.rate_lector(lector1, 'GIT', 6)

print(cool_mentor)
print(lector1)
print(best_student)
print(cool_mentor == lector1)
print(best_student == worst_student)


# проверка средней оценки для студента
print('Средняя оценка у студентов за курс Python')
print(hw_for_course('Python'))

# проверка средней оценки для лектора
print('Средняя оценка у Some Buddy за курс Python')
print(lection_for_course('Python'))    

# тест функции на ошибку
print('Средняя оценка у ревьюера')
print(average_for_course(even_cooler_mentor, 'Python'))