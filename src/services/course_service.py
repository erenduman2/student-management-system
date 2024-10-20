import logging

from ..models import Course, Student, Lecturer
from ..repositories import CourseRepository

class CourseService:
    def __init__(self, course: Course):
        """
        :param course:
        :type course: Course
        """
        self.course = course
        self.course_rep = CourseRepository(course)

    def create_course(self):
        """Create new course. Check if exist before."""

        if self.exists():
            logging.warning("Course {} already exists".format(self.course.id))
        else:
            self.course_rep.create()


    def delete_course(self):
        """Delete course."""
        if self.exists():
            self.course_rep.delete()
        else:
            logging.warning("Course {} does not exist".format(self.course.id))

    # def enroll_student(self, student):
    #     """Enroll student to the course.
    #     Used functions: is_quota_full (in Course Class)
    #     :param student:
    #     :type student: Student
    #     """
    #     student_service = StudentService(student)
    #     if self.exists() and student_service.exists():
    #         if not self.is_quota_full():
    #             is_enrolled = student_service.enroll_to_course(self.course)
    #             if is_enrolled:
    #                 logging.info("Student {} {} successfully enrolled for the course {}.".format(student.first_name, student.last_name, self.course.name))
    #             else:
    #                 logging.warning("Student {} {} failed to enroll for the course {}.".format(student.first_name, student.last_name, self.course.name))
    #     else:
    #         logging.warning("Course {} or Student {} does not exist.".format(self.course.id, student.student_id))

    def enroll_student(self, student: Student):
        """Enroll a student to the course.
        Used functions: is_quota_full (in Course Class)
        :param student:
        :type student: Student
        """
        self.course_rep.enroll_student(student)

    def is_quota_full(self):
        """ Check if course is full.
        :return:
        :rtype: bool
        """
        if self.course.current_quota >= self.course.max_quota:
            logging.info("Quota of the course {} is full".format(self.course.name))
            return True
        else:
            return False

    def exists(self):
        if self.course_rep.exists():
            return True
        else:
            logging.warning("Course {} does not exist".format(self.course.id))
            return False

    def assign_a_teacher(self, lecturer: Lecturer):
        self.course_rep.assign_a_teacher(lecturer)