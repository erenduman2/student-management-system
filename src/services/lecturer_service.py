import logging

from .course_service import CourseService
from ..models.course import Course
from ..models.lecturer import Lecturer
from ..models.student import Student
from ..repositories.lecturer_repository import LecturerRepository


class LecturerService:

    def __init__(self, lecturer):
        """
        :param lecturer:
        :type lecturer: Lecturer
        """
        self.lecturer = lecturer
        self.lecturer_rep = LecturerRepository(lecturer)



    def create_lecturer(self):
        """Create a new Lecturer.
        :return:
        """
        self.lecturer_rep.create()

    def delete_lecturer(self):
        """Delete a Lecturer.
        """
        self.lecturer_rep.delete()

    def assign_to_course(self, course):
        """Assign a lecturer to the course. Check if the lecturer and course exists.
        :param course:
        :type course: Course
        :return:
        """
        course_service = CourseService(course)
        if self.exists() and course_service.exists():
            self.lecturer_rep.assign_a_course(course)
            course_service.assign_a_teacher(self.lecturer)
        else:
            logging.warning("Lecturer {} {} or Course {} does not exist.".format(self.lecturer.first_name, self.lecturer.last_name, course.name))

    def exists(self):
        """ Check if lecturer exists.
        :return:
        :rtype: bool
        """
        return self.lecturer_rep.exists()

    def get_weekly_schedule(self):
        """Get dates, times, and places of the courses that lecturer is giving.
        :return:
        """