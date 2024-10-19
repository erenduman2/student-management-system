from ..models.course import Course
from ..models.lecturer import Lecturer
from ..models.student import Student
from ..repositories.student_repository import StudentRepository


class StudentService:

    def __init__(self, student):
        self.student = student
        self.student_rep = StudentRepository(student)

    def create_student(self):
        self.student_rep.create()


    def delete_student(self):
        self.student_rep.delete()

    # @staticmethod
    # def enroll_to_course(student_number, course_id):
        """Enroll student to course. Check if that student eligible to take that course.
        Algorithm:
            Read the student from DB and Create new student object with the data from DB.
            Read the course from DB and Create new course object with the data from DB.
            Check if that student eligible to take that course with the METHODS from student class. (is_credit_limit_exceeded)
            Course eligibility will be checked. (is_quota_full, inside the Course Class)
            Pass objects to the method in CourseService. (enroll_student)
            If everything's okay:
                That student data(taken_courses, course_count, credit_count) will be UPDATED with the new student object.
                Updates about course will be done by updating the quota and enrolled students. There's not going to be course object.
        :param student_number:
        :param course_id:
        :return:
        """

    def get_weekly_schedule(self):
        """Get dates, times, and places of the courses that student is taking.
        """

    def enroll_to_course(self, course):
        """
        :param course:
        :type course: Course
        :return: True if student enrolled, false otherwise.
         :rtype: bool
        """
        if self.can_take_the_course(course):
            self.student_rep.enroll_to_course(course)
            return True
        else:
            return False

    def can_take_the_course(self, course):
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


    def is_any_course_overlaps(self, course):
        """Check if given course overlaps with any other course.
        :param course:
        :type course: Course
        """

    def is_credit_limit_exceeded(self, course):
        """Check if that student will exceed his/her credit limit with the new course_credit given.
        :param course:
        :type course: Course
        :return
        """

    def exists(self):
        return self.student_rep.exists()
