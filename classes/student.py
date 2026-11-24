class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, starting_date, course, grades):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.starting_date = starting_date
        self.course = course
        self.grades = grades

    def display_name(self):
        print(self.first_name, self.last_name)

    def update_grade(self, course, new_grade):
        self.grades[course] = new_grade

    def get_info(self):
        return self.first_name, self.last_name

    def calculate_final_grade(self):
        