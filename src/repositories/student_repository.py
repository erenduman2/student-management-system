

class StudentRepository:
    def __init__(self, student):
        """Connect to DB.
        :param student: Student object
        :type student: Student
        """
        self.student = student

    def create(self):
        """Create new student in DB."""

    @staticmethod
    def read(student_id):
        """Read student in DB.
        :param student_id: Student ID
        :type student_id: int
        :return: Student object
        :rtype: Student
        """

    def delete(self):
        """Delete student in DB."""

    def update(self):
        """Update student in DB."""

    def exists(self):
        """Check if student exists in DB."""

    def get_courses(self):
        """Get courses that student has enrolled."""

    def enroll_to_course(self, course):
        """Enroll student to course."""