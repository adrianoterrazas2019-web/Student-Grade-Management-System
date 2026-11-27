class Course:

    def __init__(self, course_id, course_name, teacher, number_of_students, degree_programme, study_level):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher = teacher
        self.number_of_students = number_of_students
        self.degree_programme = degree_programme
        self.study_level = study_level

    def display_name (self):
        print(self.course_name)

    def update_teacher (self, teacher):
        self.teacher = teacher

    def get_course_info (self):
        return self.course_id, self.course_name, self.teacher, self.number_of_students, self.degree_programme,self.study_level

    def calculate_average_grade (self, students):
        total = 0 
        count = 0
        for student in students:

            if self.course_name in student.grades:
                total = total + student.grades[self.course_name]
                count = count + 1

        if count == 0: 
            return 0

        return total / count

        