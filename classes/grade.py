class Grade:
    def __init__(self, grade_id, student_id, course_id, grade):
        self.grade_id = grade_id
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade

    def display_grade(self):
        print(self.grade)

    def update_grade(self, new_grade):

        if new_grade < 0 or new_grade > 100:
            print ("Invalid grade")
        else:
            self.grade = new_grade
            print ("Valid grade")

    def get_info(self):
        return self.grade_id, self.student_id, self.course_id, self.grade

    def is_valid_grade(self):
        if self.grade < 0 or self.grade > 100:
            return False
        else:
            return True

