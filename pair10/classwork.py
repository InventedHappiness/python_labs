class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return self.name

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def info(self):
        return f'{self.name}, {self.group}'

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f'{self.name}, {self.subject}'

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
    def add_student(self, student):
        self.students.append(student)


student1 = Student("Anna", "10IT")
course2 = Course("Maths", "10IT")
course2.add_student(student1)
person = Person("Ivan")
teacher = Teacher("Mariia", "math")
student2 = Student("Matvey", "10IT")
course2.add_student(student2)

for student in course2.students:
    student.info()

# print(course.name)
# print(course.teacher.info())
# print(course.students)


# print(student.name)
# print(student.group)
# print(person.info())
# print(person.info())
# print(student.info())
# print(teacher.info())

# print(isinstance(student, Student))
