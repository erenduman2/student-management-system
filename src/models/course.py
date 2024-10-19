class Course:
    """A class to hold information about a course.
    Instance variables: course_name, course_name, course_id, credit, max_quota,
                        student_count, lecturer, term, date, time, is_active
    """
    def __init__(self, name, id, credit, max_quota, student_count, lecturer, term, date, time, is_active):
        self.name = name
        self.id = id
        self.credit = credit
        self.max_quota = max_quota
        self.student_count = student_count
        self.lecturer = lecturer
        self.term = term
        self.date = date
        self.time = time
        self.is_active = is_active
        self.current_quota = 0
        self.enrolled_students = []
