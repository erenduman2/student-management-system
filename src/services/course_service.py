import logging

from ..models.course import Course
from ..models.lecturer import Lecturer
from ..models.student import Student
from ..repositories.course_repository import CourseRepository
from ..services.student_service import StudentService

class CourseService:
    def __init__(self, course):
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

    def enroll_student(self, student):
        """Enroll student to the course.
        Used functions: is_quota_full (in Course Class)
        :param student:
        :type student: Student
        """
        student_service = StudentService(student)
        if self.exists() and student_service.exists():
            if not self.is_quota_full():
                is_enrolled = student_service.enroll_to_course(self.course)
                if is_enrolled:
                    logging.info("Student {} {} successfully enrolled for the course {}.".format(student.first_name, student.last_name, self.course.name))
                else:
                    logging.warning("Student {} {} failed to enroll for the course {}.".format(student.first_name, student.last_name, self.course.name))
        else:
            logging.warning("Course {} or Student {} does not exist.".format(self.course.id, student.student_id))

    def is_quota_full(self):
        """ Check if course is full.
        :return:
        :rtype: bool
        """
        return self.course.current_quota >= self.course.max_quota

    def exists(self):
        return self.course_rep.exists()