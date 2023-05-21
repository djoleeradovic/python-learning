class Student():
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Coures():
    def __init__(self,name,max_students):
        self.name = name
        self.max_studnets = max_students
        self.students = []

    def add_student(self,student):
        if len(self.students) < self.max_studnets:
            self.students.append(student)
            return True
        return False
    
    def avg_grade(self):
        grade = 0
        for student in self.students:
            grade += student.get_grade()
        return grade / len(self.students)
    
    def get_students_info(self):
        for i in self.students:
            print(f"Name: {i.name} \nYears: {i.age} \nGrade: {i.grade}\nCourse: {course.name}")
            print("-----------------")

s1 = Student("Mark",19,10)
s2 = Student("Alex",19,8)
s3 = Student("Josh",19,6)

course = Coures("Math",3)
course.add_student(s1)
course.add_student(s2)
