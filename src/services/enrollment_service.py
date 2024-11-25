import logging

from ..models import Student, Course
from ..services import StudentService, CourseService
class EnrollmentService:
    def __init__(self):
        pass

    @staticmethod
    def enroll(student_id, course_id):
        """Enroll student to a course.
        :param student_id:
        :type student_id: Student
        :param course_id:
        :type course_id: Course
        :return:
        """
        student_service = StudentService(student)
        course_service = CourseService(course)
        if student_service.exists() and course_service.exists():
            if (not course_service.is_quota_full()) and (student_service.can_take_the_course(course)):
                course_service.enroll_student(student)
                student_service.enroll_to_course(course)
            else:
                logging.warning("Enrolling to the course is not successful")
        else:
            logging.warning("Enrolling to the course is not successful")
