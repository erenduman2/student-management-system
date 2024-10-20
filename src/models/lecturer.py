class Lecturer:
    """A class to hold information about a teacher.
    Instance variables: first_name, last_name, id_number, gender, birth_date, phone_number, email
    """
    def __init__(self, first_name, last_name, id_number, gender, birth_date, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.gender = gender
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.email = email
        self.active_given_lessons = 0  # Courses that are currently given by the teacher.