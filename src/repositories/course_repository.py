

class CourseRepository:
    def __init__(self, course):
        """Connect to DB
        :param course:
        :type course: Course
        :return:
        """
        self.course = course

    def create(self):
        """Create new course in DB."""

    def read(self):
        """Read course in DB."""

    def delete(self):
        """Delete course in DB."""

    def update(self):
        """Update course in DB."""

    def exists(self):
        """Check if course exists in DB."""

    def enroll_a_student(self, student_id):
        """Enroll student to a course"""

    def is_student_enrolled(self, student):
        """Check if student is enrolled in DB."""
