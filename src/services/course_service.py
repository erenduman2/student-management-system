import logging
from typing import Union

from sqlalchemy import select, exists
from sqlalchemy.exc import IntegrityError

from src.models import Course, Lecturer, Student, student_course


class CourseService:
    def __init__(self, db_session):
        self.db_session = db_session

    #  Needs to be created with code, name, credit, quota params. Other attributes like students or lecturer will be
    #  assigned specifically.
    def create_course(self, course_data: dict) -> bool:
        """
        Create a student and return True if successful.

        Keyword arguments:
            course_data -- Dictionary of course data
        """

        if self.exists(course_data["code"]):
            logging.warning("Course {} already exists".format(course_data["code"]))
            return False
        else:
            code = course_data['code']
            name = course_data['name']
            credit = course_data['credit']
            quota = course_data['quota']
            new_course = Course(code=code, name=name, credit=credit, quota=quota)

            try:
                with self.db_session as session:
                    session.add(new_course)
                    session.commit()
                    logging.info("Course with code {} created successfully".format(code))
                    return True
            except IntegrityError as e:
                print("IntegrityError: ", e)
                return False
            except Exception as e:
                print(e)
                return False

    def assign_lecturer(self, course_code: str, lecturer_id: int) -> bool:
        """
        Assign a lecturer to a course. Return True if successful.

        Keyword arguments:
            course_code -- Course code
            lecturer_id -- Lecturer id
        """
        try:
            with self.db_session as session:
                # lecturer = session.execute(select(Course.lecturer).filter_by(code=course_code))
                lecturer = session.execute(select(Lecturer).filter_by(id=lecturer_id)).scalar_one()
                course = session.execute(select(Course).filter_by(code=course_code)).scalar_one()
                course.lecturer = lecturer
                course.lecturer.id = lecturer.id
                session.commit()
                return True
        except Exception as e:
            logging.error(e)
            return None

    def get_lecturer(self, course_code: str) -> Lecturer:
        """
        Get lecturer of a course. Return lecturer object if successful.
        Keyword arguments:
            course_code -- Course code
        """
        with self.db_session as session:
            course = session.execute(select(Course).filter_by(code=course_code)).scalar_one()
            return course.lecturer

    def delete_course(self, course_code: str) -> bool:
        """
        Delete a course. Return True if successful.

        Keyword arguments:
            course_code -- Course code
        """
        if self.exists(course_code):
            with self.db_session as session:
                course = session.execute(select(Course).where(Course.code == course_code)).scalar_one()
                session.delete(course)
                print("Deleting...")
                session.commit()
                print("Deleted.")
                return True
        else:
            logging.warning("Course {} does not exist".format(course_code))
            return False

    #  Some can only update name, credit or quota with this function. The others should be done via other functions.
    def update_course(self, code: str, name=None, credit=None, quota=None) -> bool:
        """
        Update a course. Return True if successful.

        Keyword arguments:
            code -- Course code
        """
        if self.exists(code):
            with self.db_session as session:
                course = session.execute(select(Course).where(Course.code == code)).scalar_one()
                if name is not None:
                    course.name = name
                if credit is not None:
                    course.credit = credit
                if quota is not None:
                    course.quota = quota
                new_course = session.execute(select(Course).where(Course.code == code)).scalar_one()
                print("updated data: ", new_course.name, new_course.credit, new_course.quota)
                session.commit()
                logging.info("Course with code {} updated successfully".format(code))
                return True
        else:
            logging.warning("Course {} does not exist".format(code))
            return False

    def exists(self, course_code: str) -> Course | None:
        """
        Check if a course exists.

        Keyword arguments:
            course_code -- Course code
        """
        with self.db_session as session:
            result = session.query(exists().where(Course.code == course_code)).scalar()
            return result

    #  Ogrenciler sadece yazdırılıyor, gerekli ise return yap.
    def get_enrolled_students(self, course_code: str) -> list[Student]:
        """
        Find and return enrolled students of a course.

        Keyword arguments:
            course_code -- Course code
        """
        all_students = []
        with self.db_session as session:
            # students = session.execute(select(Course.enrolled_students).where(Course.code == course_code).where(Student.id == Course.enrolled_students.id))
            students = session.execute(select(Student).join(student_course).join(Course).where(Course.code == course_code)).all()
            for student in students:
                for row in student:
                    print(row.name)
                    all_students.append(row)
        return all_students
