import logging

from sqlalchemy import exists, select
from sqlalchemy.exc import IntegrityError

from src.models import Course, Student, student_course


class StudentService:

    def __init__(self, db_session):
        self.db_session = db_session

    def create_student(self, student_data):
        if self.exists(student_data["ssn"]):
            logging.warning("Student {} already exists".format(student_data["ssn"]))
            return False
        else:
            name = student_data['name']
            surname = student_data['surname']
            ssn = student_data['ssn']
            new_student = Student(name=name, surname=surname, ssn=ssn)

            try:
                with self.db_session as session:
                    session.add(new_student)
                    session.commit()
                    # logging.info("Lecturer with ssn {} created successfully".format(ssn))
                    print("Student with ssn {} created successfully".format(ssn))
                    return True
            except IntegrityError as e:
                print("IntegrityError: ", e)
                return False
            except Exception as e:
                print(e)
                return False

    def delete_student(self, student_ssn):
        if self.exists(student_ssn):
            with self.db_session as session:
                student = session.execute(select(Student).where(Student.ssn == student_ssn)).scalar_one()
                session.delete(student)
                print("Deleting..")
                session.commit()
                print("Deleted")
                return True
        else:
            logging.warning("Student {} does not exist".format(student_ssn))
            return False

    #  st ve cr varlığı kontrol edilmeli
    def enroll_to_course(self, student_ssn, course_code):
        #  if koşullar sağlanmışSA
        with self.db_session as session:
            student = session.execute(select(Student).where(Student.ssn == student_ssn)).scalar_one()
            course = session.execute(select(Course).where(Course.code == course_code)).scalar_one()

            student.enrolled_courses.append(course)
            student.active_credit_count = student.active_credit_count + course.credit

            course.enrolled_students.append(student)
            course.student_count += 1

            session.commit()
            print("Student {} is enrolled to the course {}.".format(student.name, course.name))
            return True

    def course_deregister(self, st_id, cr_id):
        with self.db_session as session:
            student = session.execute(select(Student).where(Student.id == st_id)).scalar_one()
            course = session.execute(select(Course).where(Course.id == cr_id)).scalar_one()
            course.enrolled_students.remove(student)
            session.commit()
            print("Student {} is removed from the course {}.".format(student.name, course.name))
            return True

    def get_courses(self, student_ssn):
        all_courses = []
        with self.db_session as session:
            courses = session.execute(select(Course).join(student_course).join(Student).where(Student.ssn == student_ssn)).all()
            for course in courses:
                for row in course:
                    print("GET STUDENT COURSES: ", row.name)
                    all_courses.append(row)

        return all_courses

    def exists(self, ssn: str):
        with self.db_session as session:
            result = session.query(exists().where(Student.ssn == ssn)).scalar()
            return result

    #  YAPILMADI
    def get_weekly_schedule(self):
        """Get dates, times, and places of the courses that student is taking."""

    #  Yapılmayacak
    def can_take_the_course(self, course: Course):
        """
        Check if that student can take the course.
        Use two functions: is_credit_limit_exceeded and is_any_course_overlaps.
        :param course:
        :type course: Course
        :return: Boolean indicating if the student can take the course.
        :rtype: bool
        """
        if (not self.is_any_course_overlaps(course)) and (not self.is_credit_limit_exceeded(course)):
            return True
        else:
            return False

    #  Yapılmayacak
    def is_any_course_overlaps(self, course: Course):
        """Check if given course overlaps with any other course.
        :param course:
        :type course: Course
        """

    #  Yapılmayacak
    def is_credit_limit_exceeded(self, course: Course):
        """Check if that student will exceed his/her credit limit with the new course_credit given.
        :param course:
        :type course: Course
        :return
        """
