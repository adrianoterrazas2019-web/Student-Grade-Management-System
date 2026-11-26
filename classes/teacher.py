class Teacher:
    def __init__(self, teacher_id, first_name, last_name, department, courses, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.courses = courses 
        self.email = email

    def display_name(self):
        print(self.first_name, self.last_name)

    def update_email(self, email):
        self.email = email

    def get_info(self):
        return self.teacher_id, self.first_name, self.last_name, self.department, self.courses, self.email

    def count_courses(self):
        return len(self.courses)