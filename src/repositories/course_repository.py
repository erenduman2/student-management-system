from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.models import Course, Lecturer


class CourseRepository:

    # global_var = declare

    @classmethod
    def create_course(cls, course_data, db_session):
        """Create new course in DB."""
        lecturer_id = course_data['lecturer_id']
        code = course_data['code']
        name = course_data['name']
        credit = course_data['credit']
        quota = course_data['quota']
        student_count = course_data['student_count']
        new_course = Course(lecturer_id=lecturer_id, code=code, name=name, credit=credit, quota=quota, student_count=student_count)

        try:
            with db_session as db:
                db.add(new_course)
                db.commit()
                print("Course with code {} created successfully".format(code))
                return True
        except IntegrityError as e:
            print("IntegrityError: ", e)
            return None
        except Exception as e:
            print(e)
            return None

    @classmethod
    def read_by_code(cls, code, db_session):
        # passBLM1091
        try:
            with db_session as db:
                # course = db.execute(select(Course.quota).where(Course.name == name)).scalar_one()
                course = db.execute(select(Course).filter_by(code=code)).scalar_one()
                # course = db.get(Course, 1)

                # course = db.get(Course, {"id": 1})
                # db.flush()
                return course
        except Exception as e:
            print("IntegrityError: ", e)
            return None

    @classmethod
    def read_by_name(cls, name, db_session):
        # passBLM1091
        try:
            with db_session as db:
                # course = db.execute(select(Course.quota).where(Course.name == name)).scalar_one()
                course = db.execute(select(Course).filter_by(name=name)).scalar_one()
                # course = db.get(Course, 1)

                # course = db.get(Course, {"id": 1})
                # db.flush()
                return course
        except Exception as e:
            print("IntegrityError: ", e)
            return None

    @classmethod
    def update_quota(cls, course_code, quota, db_session):
        """Update course in DB."""
        try:
            with db_session as db:
                course = db.execute(select(Course).where(Course.code == course_code)).scalar_one()
                course.quota = quota
                course_quota = db.execute(select(Course.name).where(Course.code == course_code)).scalar_one()
                print(course_quota)
                db.commit()
                print("Course with code {} updated successfully".format(course_code))
                return True
        except Exception as e:
            print("Error: ", e)
            return False

    @classmethod
    def delete_course(cls, course_code, db_session):
        try:
            with db_session as db:
                course = db.execute(select(Course).where(Course.code == course_code)).scalar_one()
                db.delete(course)
                print("Deleting...")
                db.commit()
                print("Deleted.")
                return True
        except Exception as e:
            print("Error: ", e)
            return False

    @classmethod
    def exists(cls, course_code, db_session):
        """Check if course exists in DB."""
        try:
            with db_session as db:
                course = db.execute(select(Course).where(Course.code == course_code)).scalar_one()
                if not course:
                    return False
                else:
                    return True
        except Exception as e:
            print("Error: ", e)

    @classmethod
    def update_credit(cls, course_data, db_session):
    # değiştirilebilir
        """Update course in DB."""
        try:
            with db_session as db:
                course = db.execute(select(Course).where(Course.code == course_data['code'])).scalar_one()
                course.name = course_data['name']
                course_name = db.execute(select(Course.name).where(Course.code == course_data['code'])).scalar_one()
                print(course_name)
                db.commit()
                print("Course with code {} updated successfully".format(course_data["code"]))
                return True
        except Exception as e:
            print("Error: ", e)
            return False

    @classmethod
    def assign_a_teacher(cls, course_code: str, lecturer: Lecturer, db_session):
        """Assign teacher to course"""
        try:
            with db_session as db:
                course = db.execute(select(Course).where(Course.code == course_code)).scalar_one()
                course.lecturer = lecturer
                db.commit()
                print("Teacher assigned to course {}".format(course_code))
                return True
        except Exception as e:
            print("Error: ", e)
            return False

    @classmethod
    def enroll_student(cls):
        """Enroll student to a course"""


