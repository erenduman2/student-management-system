from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.models import Course, Lecturer


class CourseRepository:

    # global_var = declare
    def __init__(self, db_session):
        self.db_session = db_session

    def read_all(self, course_code):
        # passBLM1091
        try:
            with self.db_session as db:
                courses = db.execute(select(Course.lecturer))
                # courses = db.get(Course, 1)
                # courses = course.fetchall()
                # for row in course:
                #     print("name: ", row.name)
                for row in courses:
                    print("name: ", row)
                return courses
        except Exception as e:
            print("Error: ", e)
            return None


    def create(self, course_data: dict):
        """Create new course in DB."""
        lecturer_id = course_data['lecturer_id']
        code = course_data['code']
        name = course_data['name']
        credit = course_data['credit']
        quota = course_data['quota']
        student_count = course_data['student_count']
        new_course = Course(lecturer_id=lecturer_id, code=code, name=name, credit=credit, quota=quota, student_count=student_count)

        try:
            with self.db_session as db:
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

    def read_by_code(self, code: str):
        # passBLM1091
        try:
            with self.db_session as db:
                # course = db.execute(select(Course.quota).where(Course.name == name)).scalar_one()
                course = db.execute(select(Course).filter_by(code=code)).scalar_one()
                # course = db.get(Course, 1)

                # course = db.get(Course, {"id": 1})
                # db.flush()
                return course
        except Exception as e:
            print("IntegrityError: ", e)
            return None

    def read_by_name(self, name: str):
        # passBLM1091
        try:
            with self.db_session as db:
                # course = db.execute(select(Course.quota).where(Course.name == name)).scalar_one()
                course = db.execute(select(Course).filter_by(name=name)).scalar_one()
                # course = db.get(Course, 1)

                # course = db.get(Course, {"id": 1})
                # db.flush()
                return course
        except Exception as e:
            print("IntegrityError: ", e)
            return None

    def update_quota(self, course_code: str, quota: int):
        """Update course in DB."""
        try:
            with self.db_session as db:
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

    def delete(self, course_code: str):
        try:
            with self.db_session as db:
                course = db.execute(select(Course).where(Course.code == course_code)).scalar_one()
                db.delete(course)
                print("Deleting...")
                db.commit()
                print("Deleted.")
                return True
        except Exception as e:
            print("Error: ", e)
            return False

    def exists(self, course_code: str):
        """Check if course exists in DB."""
        try:
            with self.db_session as db:
                course = db.execute(select(Course).where(Course.code == course_code)).scalar_one()
                if not course:
                    return False
                else:
                    return True
        except Exception as e:
            print("Error: ", e)

    def update_credit(self, course_data: dict):
    # değiştirilebilir
        """Update course in DB."""
        try:
            with self.db_session as db:
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

    def assign_a_teacher(self, course_code: str, lecturer: Lecturer):
        """Assign teacher to course"""
        try:
            with self.db_session as db:
                course = db.execute(select(Course).where(Course.code == course_code)).scalar_one()
                course.lecturer = lecturer
                db.commit()
                print("Teacher assigned to course {}".format(course_code))
                return True
        except Exception as e:
            print("Error: ", e)
            return False

    def enroll_student(self):
        """Enroll student to a course"""