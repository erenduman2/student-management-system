import logging

from sqlalchemy import exists, select
from sqlalchemy.exc import IntegrityError

# from course_service import CourseService
from src.models import Course, Lecturer, student_course, Student


# from src.services import CourseServices


# from .repositories import LecturerRepository


class LecturerService:

    def __init__(self, db_session):
        """
        :param lecturer:
        :type lecturer: Lecturer
        """
        self.db_session = db_session


    #  Params are only name, surname and ssn. Other should be updated with other functions.
    def create_lecturer(self, lecturer_data: dict) -> bool:
        """
        Create a new lecturer and return True if successful.

        Keyword arguments:
            lecturer_data -- Dictionary of lecturer data.
        """
        assert "ssn" in lecturer_data, "SSN is mandatory"

        if self.exists(lecturer_data["ssn"]):
            logging.warning("Lecturer {} already exists".format(lecturer_data["ssn"]))
            return False
        else:
            name = lecturer_data['name']
            surname = lecturer_data['surname']
            ssn = lecturer_data['ssn']
            new_lecturer = Lecturer(name=name, surname=surname, ssn=ssn)

            try:
                with self.db_session as session:
                    session.add(new_lecturer)
                    session.commit()
                    # logging.info("Lecturer with ssn {} created successfully".format(ssn))
                    print("Lecturer with ssn {} created successfully".format(ssn))
                    return True
            except IntegrityError as e:
                print("IntegrityError: ", e)
                return False
            except Exception as e:
                print(e)
                return False

    def delete_lecturer(self, lecturer_ssn: str) -> bool:
        """
        Delete an existing lecturer and return True if successful.

        Keyword arguments:
            lecturer_ssn -- SSN of the lecturer.
        """
        if self.exists(lecturer_ssn):
            with self.db_session as session:
                lecturer = session.execute(select(Lecturer).where(Lecturer.ssn == lecturer_ssn)).scalar_one()
                session.delete(lecturer)
                print("Deleting..")
                session.commit()
                print("Deleted")
                return True
        else:
            logging.warning("Lecturer {} does not exist".format(lecturer_ssn))

    def add_course(self, course_code: str, lecturer_ssn: str) -> bool :
        """Assign a lecturer to the course. Check if the lecturer and course exists. Return True if successful.

        Keyword arguments:
            course_code -- Course code.
            lecturer_ssn -- SSN of the lecturer.
        """
        try:
            with self.db_session as session:
                # lecturer = session.execute(select(Course.lecturer).filter_by(code=course_code))
                lecturer = session.execute(select(Lecturer).filter_by(ssn=lecturer_ssn)).scalar_one()
                course = session.execute(select(Course).filter_by(code=course_code)).scalar_one()
                course.lecturer = lecturer
                course.lecturer.id = lecturer.id
                lecturer.given_courses.append(course)
                session.commit()
                return True
        except Exception as e:
            logging.error(e)
            return False

    def exists(self, lecturer_ssn: str) -> Lecturer:
        """
        Check if lecturer exists.

        Keyword arguments:
            lecturer_ssn -- SSN of the lecturer.
        """
        # return self.lecturer_rep.exists()
        with self.db_session as session:
            result = session.query(exists().where(Lecturer.ssn == lecturer_ssn)).scalar()
            return result

    def get_courses(self, lecturer_id: int) -> list[Course]:
        """
        Get courses of a lecturer and return all courses.

        Keyword arguments:
            lecturer_id -- ID of the lecturer.

        """
        with self.db_session as session:
            all_courses = []
            # courses = session.execute(select(Course).join(student_course).join(Student).where(Course.id == id)).all()
            # for course in courses:
            #     for row in course:
            #         print("GET LECTURER COURSES: ", row.name)
            #         all_courses.append(row)
            lecturer = session.execute(select(Lecturer).where(Lecturer.id == lecturer_id)).scalar_one()
            for course in lecturer.given_courses:
                all_courses.append(course)
                print(course.name)
            return all_courses


