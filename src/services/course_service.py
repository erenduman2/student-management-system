import logging

# from ..models import Course, Student, Lecturer
# from ..repositories import CourseRepository
from src.repositories import CourseRepository

class CourseService:
    def __init__(self, course_repository: CourseRepository):
        self.course_repository = course_repository

    def create_course(self, course_data):
        """Create new course. Check if exist before."""

        if self.exists(course_data["code"]):
            logging.warning("Course {} already exists".format(course_data["code"]))
        else:
            self.course_repository.create(course_data)

    def find_lecturer(self, lecturer_id, db_session):
        pass

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

    def is_quota_full(self) -> bool:
        """ Check if course is full and return True or False.
        :return:
        :rtype: bool
        """
        if self.course.current_quota >= self.course.max_quota:
            logging.info("Quota of the course {} is full".format(self.course.name))
            return True
        else:
            return False

    def exists(self, course_code: str):
        if self.course_repository.exists(course_code):
            return True
        else:
            logging.warning("Course {} does not exist".format(course_code))
            return False

    def assign_a_teacher(self, lecturer: Lecturer):
        self.course_rep.assign_a_teacher(lecturer)