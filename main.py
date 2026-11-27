"""my new project"""

from classes.student import Student
from classes.teacher import Teacher
from classes.course import Course
from classes.grade import Grade

def main():
    print("This is my GISMA Python Project!")

if __name__ == '__main__':
    main()

student1 = Student (1001, "Leandro", "Terrazas", "15/8/2006", "01/10/2026",["Python", "Databases"], {"Python": 80, "Data Bases": 90 , "Data Structures": 85})

student1.display_name()
print (student1.get_info())

student1.update_grade ("Data Structures", 75)
student1.update_grade ("Python", 95)
print(student1.grades)

student2 = Student (1002, "Leandro", "Terrazas", "15/8/2006", "01/10/2026",["Python", "Databases"], {"Python": 75, "Data Bases": 65} )
print(student1.grades)
print(student2.grades)

print(student1.calculate_final_grade())
print(student2.calculate_final_grade())



teacher1 = Teacher (2001, "Juan", "Vargas", "Computer Science", ["Python", "Data Bases"], "vargas@example.com")

teacher1.display_name()
print (teacher1.get_info())

teacher1.update_email ("vargas@example.com")
teacher1.update_email ("vargas@gisma.com")
print(teacher1.email)

print(teacher1.count_courses())



course1 = Course ("3001", "Python", "Juan Vargas", 25, "Data Science and AI", "Undergraduate" )
course1.display_name()

course1.update_teacher ("Jose Manuel")
print(course1.teacher)

print(course1.get_course_info())

students = [student1, student2]
print(course1.calculate_average_grade(students)) 

print(course1.calculate_average_grade([]))



grade1 = Grade (4001, 1001, "3001", 95)
grade2 = Grade (4002, 1002, "3002", 120)

grade1.display_grade()

grade1.update_grade (77)
print(grade1.grade)
grade1.update_grade (120)

print (grade1.get_info())

print (grade1.is_valid_grade())
print (grade2.is_valid_grade())

if grade2.is_valid_grade() and grade2.student_id == student1.student_id and grade2.course_id == course1.course_id:
    student1.update_grade(course1.course_name, grade2.grade)
else:
    print("Validation failed")
    
print (student1.grades)