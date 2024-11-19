import logging

from sqlalchemy import exists, select
from sqlalchemy.exc import IntegrityError

# from course_service import CourseService
from src.models import Course, Lecturer
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
    def create_lecturer(self, lecturer_data):
        """Create a new Lecturer."""
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

    def delete_lecturer(self, lecturer_ssn):
        """Delete a Lecturer.
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

    def add_course(self, course_code, lecturer_id):
        """Assign a lecturer to the course. Check if the lecturer and course exists.
        :param course_code:
        :type course_code: str
        :param lecturer_id:
        :type lecturer_id: int
        :return:
        """
        try:
            with self.db_session as session:
                # lecturer = session.execute(select(Course.lecturer).filter_by(code=course_code))
                lecturer = session.execute(select(Lecturer).filter_by(id=lecturer_id)).scalar_one()
                course = session.execute(select(Course).filter_by(code=course_code)).scalar_one()
                course.lecturer = lecturer
                course.lecturer.id = lecturer.id
                session.commit()
                return lecturer
        except Exception as e:
            logging.error(e)
            return None

    def exists(self, ssn: str):
        """ Check if lecturer exists.
        :return:
        :rtype: bool
        """
        # return self.lecturer_rep.exists()
        with self.db_session as session:
            result = session.query(exists().where(Lecturer.ssn == ssn)).scalar()
            return result

    def get_weekly_schedule(self):
        """Get dates, times, and places of the courses that lecturer is giving.
        :return:
        """