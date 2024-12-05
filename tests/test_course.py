import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.models import Course, Base
from src.services import CourseService

# Base = declarative_base()

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)
        self.course_service = CourseService(self.session)

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_create_course(self):
        valid_course_data =  dict(code="CS", name="Computer Science", credit=5, quota=30)
        self.course_service.create_course(valid_course_data)

        course = self.session.query(Course).filter(Course.code == valid_course_data["code"]).one()
        self.assertIsNotNone(course, "course could not be created")

    def test_delete_course(self):
        valid_course_data =  dict(code="CS", name="Computer Science", credit=5, quota=30)
        self.course_service.create_course(valid_course_data)

        course = self.session.query(Course).filter(Course.code == valid_course_data["code"]).one()
        self.course_service.delete_course(course.code)
        course = self.session.query(Course).filter(Course.code == valid_course_data["code"]).all()

        self.assertEquals(len(course), 0, "lecturer could not be deleted")


    def test_update_course(self):
        valid_course_data =  dict(code="CS", name="Computer Science", credit=5, quota=30)
        self.course_service.create_course(valid_course_data)

        self.course_service.update_course(valid_course_data["code"], name="CS2", credit=3, quota=20)
        course = self.session.query(Course).filter(Course.code == valid_course_data["code"]).one()

        self.assertTrue(
            all([
                course.code == valid_course_data["code"],
                course.name == "CS2",
                course.credit == 3,
                course.quota == 20
            ]),
            "course could not be updated"
        )


    def test_enroll_to_course(self):
        student_data = dict(name="Eren", surname="Duman", ssn="1")
        # course_data = dict(name)