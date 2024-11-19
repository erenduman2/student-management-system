import logging
from sqlalchemy import select, exists
from sqlalchemy.exc import IntegrityError

from src.repositories import CourseRepository
from src.models import Course, Lecturer


class CourseServices:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_course(self, course_data):
        """Create new course. Check if exist before."""

        if self.exists(course_data["code"]):
            logging.warning("Course {} already exists".format(course_data["code"]))
            return False
        else:
            lecturer_id = course_data['lecturer_id']
            code = course_data['code']
            name = course_data['name']
            credit = course_data['credit']
            quota = course_data['quota']
            student_count = course_data['student_count']
            new_course = Course(lecturer_id=lecturer_id, code=code, name=name, credit=credit, quota=quota,
                                student_count=student_count)

            try:
                with self.db_session as session:
                    session.add(new_course)
                    session.commit()
                    print("Course with code {} created successfully".format(code))
                    return True
            except IntegrityError as e:
                print("IntegrityError: ", e)
                return False
            except Exception as e:
                print(e)
                return False

    #  Bu kısımda DB işlemleri direkt olarak yapıldı. Kodların repository'ye taşınması gerekir mi diye kontrol et.
    def find_lecturer(self, course_code, db_session):
        try:
            with db_session as db:
                lecturer = db.execute(select(Course.lecturer).filter_by(code=course_code))
                return lecturer
        except Exception as e:
            logging.error(e)
            return None

    def delete_course(self, course_code):
        """Delete course."""
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
    def update_course(self, code, name=None, credit=None, quota=None):
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

    # def enroll_student(self, student):
    #     """Enroll student to the course.
    #     Used functions: is_quota_full (in Course Class)
    #     :param student:
    #     :type student: Student
    #     """
    #     student_service = StudentService(student)
    #     if self.exists() and student_service.exists():
    #         if not self.is_quota_full():
    #             is_enrolled = student_service.enroll_to_course(self.course)
    #             if is_enrolled:
    #                 logging.info("Student {} {} successfully enrolled for the course {}.".format(student.first_name, student.last_name, self.course.name))
    #             else:
    #                 logging.warning("Student {} {} failed to enroll for the course {}.".format(student.first_name, student.last_name, self.course.name))
    #     else:
    #         logging.warning("Course {} or Student {} does not exist.".format(self.course.id, student.student_id))

    # def enroll_student(self):
    #     """Enroll a student to the course.
    #     Used functions: is_quota_full (in Course Class)
    #     :param student:
    #     :type student: Student
    #     """
    #     self.course_rep.enroll_student(student)
    #
    # def assign_lecturer(self, lecturer_id, course_code):
    #     with self.db_session as session:
    #         lecturer = session.execute(select(Lecturer).filter_by(id=lecturer_id))
    #         course = session.execute(select(Course).where(Course.code == course_code))
    #         course.lecturer = lecturer
    #         session.execute()
    #
    #         session.commit()
    #
    # def is_quota_full(self) -> bool:
    #     """ Check if course is full and return True or False.
    #     :return:
    #     :rtype: bool
    #     """
    #     if self.course.current_quota >= self.course.max_quota:
    #         logging.info("Quota of the course {} is full".format(self.course.name))
    #         return True
    #     else:
    #         return False
    #
    def exists(self, course_code: str):
        with self.db_session as session:
            result = session.query(exists().where(Course.code == course_code)).scalar()

            return result
            # session.query(q.exists())

        # if self.course_repository.exists(course_code):
        #     return True
        # else:
        #     logging.warning("Course {} does not exist".format(course_code))
        #     return False
    #
    # def assign_a_teacher(self, lecturer: Lecturer):
    #     self.course_rep.assign_a_teacher(lecturer)