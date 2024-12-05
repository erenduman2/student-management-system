import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.models import Student, Base
from src.services import StudentService

# Base = declarative_base()

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)
        self.student_service = StudentService(self.session)

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_add_student(self):
        valid_student_data = dict(name="Eren", surname="Duman", ssn="1")
        self.student_service.create_student(valid_student_data)

        student = self.session.query(Student).filter(Student.ssn == valid_student_data["ssn"]).one()
        self.assertIsNotNone(student, "student could not be added")

    def test_delete_student(self):
        student_data = dict(name="Eren", surname="Duman", ssn="1")
        self.student_service.create_student(student_data)
        student = self.session.query(Student).filter(Student.ssn == student_data["ssn"]).one()
        self.student_service.delete_student(student.ssn)
        student = self.session.query(Student).filter(Student.ssn == student_data["ssn"]).all()

        self.assertEquals(len(student), 0, "lecturer could not be deleted")

    def test_enroll_to_course(self):
        student_data = dict(name="Eren", surname="Duman", ssn="1")
        # course_data = dict(name)