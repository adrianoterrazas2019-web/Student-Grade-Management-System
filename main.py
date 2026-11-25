"""my new project"""

from classes.student import Student

def main():
    print("This is my GISMA Python Project!")

if __name__ == '__main__':
    main()

student1 = Student (1001, "Leandro", "Terrazas", "15/8/2006", "01/10/2026",["Python", "Databases"], {"Python": 80, "Databases": 90 })

student1.display_name()
print (student1.get_info())

student1.update_grade ("Python", 95)
print(student1.grades)

student1.update_grade ("Python", -120)
student2 = Student (1002, "Leandro", "Terrazas", "15/8/2006", "01/10/2026",["Python", "Databases"], {} )
print(student1.grades)
print(student2.grades)

print(student1.calculate_final_grade())
print(student2.calculate_final_grade())