from sqlalchemy import select

from src.models import Course, Lecturer


class LecturerRepository:

    @classmethod
    def create_lecturer(cls, lecturer_data, db_session):
        """Create new lecturer in DB."""
        name = lecturer_data["name"]
        surname = lecturer_data["surname"]
        ssn = lecturer_data["ssn"]
        birth_date = lecturer_data["birth_date"]
        phone = lecturer_data["phone"]
        email = lecturer_data["email"]

        new_lecturer = Lecturer(name=name, surname=surname, ssn=ssn, birth_date=birth_date, phone=phone, email=email)

        try:
            with db_session as db:
                db.add(new_lecturer)
                db.commit()
                print("Lecturer {} {} created successfully".format(name, surname))
        except Exception as e:
            print("Exception: ", e)

    @classmethod
    def read_by_id(cls, lecturer_id, db_session):
        """Read lecturer in DB."""
        try:
            with db_session as db:
                lecturer = db.get(Lecturer, lecturer_id)
                return lecturer
        except Exception as e:
            print("Exception: ", e)
            return None

    @classmethod
    def update_contact(cls, lecturer_id, phone, email, db_session):
        """Update lecturer in DB."""
        try:
            with db_session as db:
                lecturer = db.get(Lecturer, lecturer_id)
                lecturer.phone = phone
                lecturer.email = email
                lecturer_phone = db.get(Lecturer, lecturer_id).phone
                print("Updated! lecturer_phone: ", lecturer_phone)
                db.commit()
                return True
        except Exception as e:
            print("Error: ", e)
            return False

    @classmethod
    def delete(cls, lecturer_id, db_session):
        """Delete lecturer in DB."""
        try:
            with db_session as db:
                lecturer = db.get(Lecturer, lecturer_id)
                db.delete(lecturer)
                print("Deleting...")
                db.commit()
                print("Deleted.")
                return True
        except Exception as e:
            print("Error: ", e)
            return False

    @classmethod
    def exists(cls, lecturer_id, db_session):
        """Check if course exists in DB."""
        try:
            with db_session as db:
                lecturer = db.get(Lecturer, lecturer_id)
                if not lecturer:
                    return False
                else:
                    return True
        except Exception as e:
            print("Error: ", e)

    @classmethod
    def assign_a_course(self, course: Course):
        """Assign a course to lecturer."""