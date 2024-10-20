from src.models import Course, Student, Lecturer


class CourseRepository:
    def __init__(self, course: Course):
        """Connect to DB
        :param course:
        :type course: Course
        :return:
        """
        self.course = course

    def create(self):
        """Create new course in DB."""

    @staticmethod
    def read(course_id: int):
        """Read course in DB.
        :param course_id:
        :type course_id: int
        :return: Course object
        :rtype: Course
        """

    def delete(self):
        """Delete course in DB."""

    def update(self):
        """Update course in DB."""

    def exists(self):
        """Check if course exists in DB."""

    def enroll_student(self, student: Student):
        """Enroll student to a course"""

    def is_student_enrolled(self, student: Student):
        """Check if student is enrolled in DB."""

    def assign_a_teacher(self, lecturer: Lecturer):
        """Assign teacher to course"""