import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.models import Student, Course, Base
from src.services import StudentService, CourseService


class TestEnrollment(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)
        self.student_service = StudentService(self.session)
        self.course_service = CourseService(self.session)

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_enroll_student(self):
        student_data = dict(name="Eren", surname="Duman", ssn="1")
        self.student_service.create_student(student_data)
        course_data =  dict(code="CS", name="Computer Science", credit=5, quota=30)
        self.course_service.create_course(course_data)

        self.student_service.enroll_to_course(student_data["ssn"], course_data["code"])

        enrolled_students = self.course_service.get_enrolled_students(course_data["code"])
        courses = self.student_service.get_courses(student_data["ssn"])

        valid_student = [student for student in enrolled_students if student.ssn == "1"]
        valid_course = [course for course in courses if course.code == "CS"]
        self.assertTrue(
            all([
                valid_student[0].ssn == "1",
                valid_course[0].code == "CS"
            ]),
            "Student not enrolled correctly"
        )
        # sonuc = [student for student in enrolled_students if student.ssn == "0"]

    def test_course_deregister(self):
        student_data = dict(name="Eren", surname="Duman", ssn="1")
        self.student_service.create_student(student_data)
        course_data = dict(code="CS", name="Computer Science", credit=5, quota=30)
        self.course_service.create_course(course_data)

        self.student_service.enroll_to_course(student_data["ssn"], course_data["code"])
        self.student_service.course_deregister(student_data["ssn"], course_data["code"])

        enrolled_students = self.course_service.get_enrolled_students(course_data["code"])
        courses = self.student_service.get_courses(student_data["ssn"])
        valid_student = [student for student in enrolled_students if student.ssn == "1"]
        valid_course = [course for course in courses if course.code == "CS"]
        self.assertTrue(
            all([
                len(valid_student) == 0,
                len(valid_course) == 0
            ]),
            "Student not deregistered correctly"
        )