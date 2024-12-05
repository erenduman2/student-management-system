import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.models import Lecturer, Course, Base
from src.services import LecturerService, CourseService


# Base = declarative_base()

class TestLecturer(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)
        self.lecturer_service = LecturerService(self.session)
        self.course_service = CourseService(self.session)

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_create_lecturer(self):
        valid_lecturer_data = dict(name="Eren", surname="Duman", ssn="1")
        self.lecturer_service.create_lecturer(valid_lecturer_data)

        lecturer = self.session.query(Lecturer).filter(Lecturer.name == valid_lecturer_data["name"]).one()
        self.assertIsNotNone(lecturer, "course could not be created")

        self.assertEqual(lecturer.surname, valid_lecturer_data["surname"], "Lecturer surname does not match")
        self.assertEqual(lecturer.ssn, valid_lecturer_data["ssn"], "Lecturer SSN does not match")

        # Test invalid data
        invalid_lecturer_data = dict(name="Eren", surname="Duman")  # Missing SSN
        with self.assertRaises(Exception) as context:
            self.lecturer_service.create_lecturer(invalid_lecturer_data)
        print(context.exception)

    def test_delete_lecturer(self):
        valid_lecturer_data = dict(name="Eren", surname="Duman", ssn="1")
        self.lecturer_service.create_lecturer(valid_lecturer_data)

        lecturer = self.session.query(Lecturer).filter(Lecturer.name == valid_lecturer_data["name"]).one()
        self.lecturer_service.delete_lecturer(lecturer.ssn)
        lecturer = self.session.query(Lecturer).filter(Lecturer.name == valid_lecturer_data["name"]).all()

        self.assertEquals(len(lecturer), 0, "lecturer could not be deleted")

    def test_add_course(self):
        valid_lecturer_data = dict(name="Eren", surname="Duman", ssn="1")
        self.lecturer_service.create_lecturer(valid_lecturer_data)
        valid_course_data = dict(code="CS", name="Computer Science", credit=5, quota=30)
        self.course_service.create_course(valid_course_data)

        self.lecturer_service.add_course(valid_course_data["code"], valid_lecturer_data["ssn"])

        courses = self.lecturer_service.get_courses(id=1)
        course = courses[0]
        lecturer = self.course_service.get_lecturer(valid_course_data["code"])


        self.assertTrue(
            all([
                course.code == valid_course_data["code"],
                lecturer.ssn == valid_lecturer_data["ssn"]
            ]),
            "course could not be added to the lecturer"
        )
