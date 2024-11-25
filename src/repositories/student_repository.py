from pydantic_core.core_schema import none_schema

from src.models import Student

class StudentRepository:

    @classmethod
    def create(cls, student_data, db_session):
        """Create new student in DB."""
        name = student_data['name']
        surname = student_data['surname']
        ssn = student_data['ssn']
        gender = student_data['gender']
        birth_date = student_data['birth_date']
        phone = student_data['phone']
        email = student_data['email']
        credit_count = student_data['credit_count']
        active_credit_count = student_data['active_credit_count']
        max_active_credit = student_data['max_active_credit']

        new_student = Student(name=name, surname=surname, ssn=ssn, gender=gender, birth_date=birth_date,
                              phone=phone, email=email, credit_count=credit_count,
                              active_credit_count=active_credit_count, max_active_credit=max_active_credit)

        try:
            with db_session as db:
                db.add(new_student)
                db.commit()
                print("New student {} {} created successfully.".format(name, surname))
                return True
        except Exception as e:
            print(e)
            return None

    @classmethod
    def read(cls, student_id, db_session):
        """Read student in DB.
        :param student_id: Student ID
        :type student_id: int
        :param db_session: DB Session
        :type db_session: sqlalchemy.orm.session.Session
        :return: Student object or null
        :rtype: Student
        """
        try:
            with db_session as db:
                student = db.get(Student, student_id)
                return student
        except Exception as e:
            print("Exception: ", e)
            return None

    @classmethod
    def update(cls, student_id, db_session):
        """Update student in DB."""

    @classmethod
    def delete(cls, student_id, db_session):
        """Delete student from DB."""
        try:
            with db_session as db:
                student = db.get(Student, student_id)
                db.delete(student)
                print("Deleting...")
                db.commit()
                print("Deleted.")
                return True
        except Exception as e:
            print("Error: ", e)
            return False

    @classmethod
    def exists(cls, student_id, db_session):
        """Check if student exists in DB."""
        try:
            with db_session as db:
                student = db.get(Student, student_id)
                if not student:
                    return False
                else:
                    return True
        except Exception as e:
            print("Error: ", e)

    def get_courses(self):
        """Get courses that student has enrolled."""

    def enroll_to_course(self):
        """Enroll student to course."""

    def graduate(self):
        """Graduate student, make the student passive."""