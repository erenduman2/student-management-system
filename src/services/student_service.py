import logging

from ..models import Course, Student
from ..repositories import StudentRepository


class StudentService:

    def __init__(self, student: Student):
        self.student = student
        self.student_rep = StudentRepository(student)

    def create_student(self):
        self.student_rep.create()


    def delete_student(self):
        self.student_rep.delete()

    def get_weekly_schedule(self):
        """Get dates, times, and places of the courses that student is taking."""

    def enroll_to_course(self, course: Course):
        """Enroll a student to the course.
        :param course:
        :type course: Course
        :return: True if student enrolled, false otherwise.
         :rtype: bool
        """
        self.student_rep.enroll_to_course(course)

    def can_take_the_course(self, course: Course):
        """Check if that student can take the course.
        Use two functions: is_credit_limit_exceeded and is_any_course_overlaps.
        :param course:
        :type course: Course
        :return: Boolean indicating if the student can take the course.
        :rtype: bool
        """
        if (not self.is_any_course_overlaps(course)) and (not self.is_credit_limit_exceeded(course)):
            return True
        else:
            return False


    def is_any_course_overlaps(self, course: Course):
        """Check if given course overlaps with any other course.
        :param course:
        :type course: Course
        """

    def is_credit_limit_exceeded(self, course: Course):
        """Check if that student will exceed his/her credit limit with the new course_credit given.
        :param course:
        :type course: Course
        :return
        """

    def exists(self):
        if self.student_rep.exists():
            return True
        else:
            logging.warning("Student {} {} does not exist".format(self.student.first_name, self.student.last_name))
            return False

