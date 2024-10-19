class Student:
    """A class to hold information about a student.
    Instance variables: first_name, last_name, id_number, gender,
                        birth_date, student_number, phone_number, email, max_active_credit
    """
    def __init__(self, first_name, last_name, id_number, gender, birth_date,
                 student_id, phone_number, email, max_active_credit):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.gender = gender
        self.birth_date = birth_date
        self.student_id = student_id
        self.phone_number = phone_number
        self.email = email
        self.active_courses = []  # A list that holds courses that student is taking currently.
        self.active_course_count = 0
        self.active_credit_count = 0
        self.max_active_credit = max_active_credit
        self.former_courses = []  # A list that holds courses that student have taken before.
        self.former_course_count = 0
        self.former_credit_count = 0
