"""my new project"""

from classes.student import Student
from classes.teacher import Teacher

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

student1.update_grade ("Python", -120)
student2 = Student (1002, "Leandro", "Terrazas", "15/8/2006", "01/10/2026",["Python", "Databases"], {} )
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