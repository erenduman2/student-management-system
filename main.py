from src.database import engine, db_session
from src.models import Base
# from src.models.deneme import student
from src.services import CourseService, StudentService, LecturerService


def main_menu():
    while True:
        try:
            choice = int(input(
                "For Student Operations Enter 1\nFor Course Operations Enter 2\nFor Lecturer Operations Enter 3\nChoice: "))
            return choice
        except ValueError:
            print("Please enter an integer")

def student_menu():
    student_service = StudentService(db_session)
    invalid_input = True
    # BU KISIMDA TUM IF'LERDE INPUT GIRILDI MI KONTROLU YAP
    while invalid_input:
        student_choice = int(input(
            "To create student 1,\nTo delete student 2,\nTo update student 3,\nTo enroll to course 4,\nTo deregister from course 5,\nTo show enrolled courses 6\nTo exit 7\nChoice: "))

        if student_choice == 1:  # Create Student
            student_data = dict()
            student_data["name"] = input("Name: ")
            student_data["surname"] = input("Surname: ")
            student_data["ssn"] = input("SSN: ")
            while student_data["name"] == "" or student_data["surname"] == "" or student_data["ssn"] == "":
                print("Please enter valid input")
                student_data["name"] = input("Name: ")
                student_data["surname"] = input("Surname: ")
                student_data["ssn"] = input("SSN: ")
            student_service.create_student(student_data)
        elif student_choice == 2:  # Delete Student
            student_ssn = input("Enter student ssn: ")
            student_service.delete_student(student_ssn)
        elif student_choice == 3:  # Update Student
            # student_service.update_student()
            pass
        elif student_choice == 4:  # Enroll to Course
            print("In order to enroll a student to a course,")
            student_ssn = input("Input Student SSN: ")
            course_code = input("Input Course Code: ")
            student_service.enroll_to_course(student_ssn, course_code)
        elif student_choice == 5:  # Deregister from Course
            print("In order to deregister a student from a course,")
            student_id = input("Input Student ID: ")
            course_code = int(input("Input Course ID: "))
            student_service.course_deregister(student_id, course_code)
        elif student_choice == 6:  # Show Enrolled Courses
            print("In order to show a student's courses,")
            student_ssn = input("Input Student SSN: ")
            student_service.get_courses(student_ssn)
        elif student_choice == 7: # burası tanımlanmalı
            invalid_input = False
        else:
            print("Please enter valid choice")
            invalid_input = True
def course_menu():
    course_service = CourseService(db_session)
    invalid_input = True
    # BU KISIMDA TUM IF'LERDE INPUT GIRILDI MI KONTROLU YAP
    while invalid_input:
        course_choice = int(input(
            "To create course 1,\nTo delete course 2,\nTo update course 3,\nTo assign lecturer 4,\nTo get lecturer 5,\nTo show enrolled students 6\nTo exit 7\nChoice: "))

        if course_choice == 1:  # Create Course
            print("Please enter course details")
            course_data = dict()
            course_data["code"] = input("Code: ")
            course_data["name"] = input("Name: ")
            course_data["credit"] = input("Credit: ")
            course_data["quota"] = input("Quota: ")
            while (course_data["code"] == "" or course_data["name"] == ""
                   or course_data["credit"] == "" or course_data["quota"] == ""):
                print("Please enter valid inputs")
                course_data["code"] = input("Code: ")
                course_data["name"] = input("Name: ")
                course_data["credit"] = input("Credit: ")
                course_data["quota"] = input("Quota: ")
            course_data["credit"] = int(course_data["credit"])
            course_data["quota"] = int(course_data["quota"])
            course_service.create_course(course_data)
        elif course_choice == 2: # Delete course
            course_code = input("Enter course code: ")
            course_service.delete_course(course_code)
        elif course_choice == 3: # Update course
            code = input("Enter course code: ")
            print("Enter name, credit or quota. Each of them is optional.")
            name = input("Name: ")
            credit = input("Credit: ")
            quota = input("Quota: ")
            if name == "":
                name = None
            if credit == "":
                credit = None
            else:
                credit = int(credit)
            if quota == "":
                quota = None
            else:
                quota = int(quota)
            course_service.update_course(code, name=name, credit=credit, quota=quota)
        elif course_choice == 4: # Assign lecturer tı the course
            course_code = input("Enter course code: ")
            lecturer_id = input("Enter lecturer id: ")
            course_service.assign_lecturer(course_code, lecturer_id)
        elif course_choice == 5: # Get lecturer
            code = input("Enter course code: ")
            lecturer = course_service.get_lecturer(code)
            print(f"Full Name: {lecturer.name} {lecturer.surname}")
        elif course_choice == 6: # show enrolled students
            code = input("Enter course code: ")
            students = course_service.get_enrolled_students(code)
            for student in students:
                print(f"Student ID: {student.id} Name: {student.name} {student.surname}")
        elif course_choice == 7:
            invalid_input = False
        else:
            print("Please enter valid choice")
            invalid_input = True
def lecturer_menu():
    lecturer_service = LecturerService(db_session)
    invalid_input = True
    # BU KISIMDA TUM IF'LERDE INPUT GIRILDI MI KONTROLU YAP
    while invalid_input:
        lecturer_choice = int(input(
            "To create lecturer 1,\nTo delete lecturer 2,\nTo add course 3,\nTo get courses 4,\nTo get weekly schedule 5,\nTo exit 6\nChoice: "))

        if lecturer_choice == 1:  # Create lecturer
            print("Please enter course details")
            lecturer_data = dict()
            lecturer_data["name"] = input("Name: ")
            lecturer_data["surname"] = input("Surname: ")
            lecturer_data["ssn"] = input("SSN: ")

            while lecturer_data["name"] == "" or lecturer_data["surname"] == "" or lecturer_data["ssn"] == "":
                print("Please enter valid inputs")
                lecturer_data["name"] = input("Name: ")
                lecturer_data["surname"] = input("Surname: ")
                lecturer_data["ssn"] = input("SSN: ")

            lecturer_service.create_lecturer(lecturer_data)
        elif lecturer_choice == 2:  # Delete lecturer
            lecturer_ssn = input("Enter lecturer SSN: ")
            lecturer_service.delete_lecturer(lecturer_ssn)
        elif lecturer_choice == 3:  # Add course to lecturer
            lecturer_id = int(input("Enter lecturer ID: "))
            course_code = input("Enter course code: ")

            lecturer_service.add_course(course_code, lecturer_id)
        elif lecturer_choice == 4:  # Get lecturer's courses
            lecturer_id = int(input("Enter lecturer id: "))
            courses = lecturer_service.get_courses(lecturer_id)
            for course in courses:
                print(f"Course code: {course.code} Course Name: {course.name}")
        elif lecturer_choice == 5:  # Get weekly schedule
            print("Daha yazılmadı")
        elif lecturer_choice == 6:
            invalid_input = False
        else:
            print("Please enter valid choice")
            invalid_input = True


def main():
    print("Welcome to Student Management System")

    while True:
        choice = main_menu()
        #  IF STUDENT
        if choice == 1:     # if student
            student_menu()
        elif choice == 2:   # if course
            course_menu()
        elif choice == 3:   # if lecturer
            lecturer_menu()


Base.metadata.create_all(engine)
main()

#  course data
# course_service = CourseService(db_session)
# course_data1 = dict()
# course_data1["code"] = "B1"
# course_data1["name"] = "BLM1"
# course_data1["credit"] = 3
# course_data1["quota"] = 50
# course_data2 = dict()
# course_data2["code"] = "B2"
# course_data2["name"] = "BLM2"
# course_data2["credit"] = 3
# course_data2["quota"] = 50
# course_data3 = dict()
# course_data3["code"] = "B3"
# course_data3["name"] = "BLM3"
# course_data3["credit"] = 3
# course_data3["quota"] = 50
# course_service.create_course(course_data1)
# course_service.create_course(course_data2)
# course_service.create_course(course_data3)

#  student data
# student_service = StudentService(db_session)
# student_data1 = dict()
# student_data1['name'] = "S1"
# student_data1['surname'] = "Student1"
# student_data1['ssn'] = 1
# student_data2 = dict()
# student_data2['name'] = "S2"
# student_data2['surname'] = "Student2"
# student_data2['ssn'] = 2
# student_data3 = dict()
# student_data3['name'] = "S3"
# student_data3['surname'] = "Student3"
# student_data3['ssn'] = 3
# student_service.create_student(student_data1)
# student_service.create_student(student_data2)
# student_service.create_student(student_data3)

#  lecturer data
# lecturer_service = LecturerService(db_session)
# lecturer_data1 = dict()
# lecturer_data1["name"] = "L1"
# lecturer_data1["surname"] = "Lecturer1"
# lecturer_data1["ssn"] = 1
# lecturer_data2 = dict()
# lecturer_data2["name"] = "L2"
# lecturer_data2["surname"] = "Lecturer2"
# lecturer_data2["ssn"] = 2
# lecturer_data3 = dict()
# lecturer_data3["name"] = "L3"
# lecturer_data3["surname"] = "Lecturer3"
# lecturer_data3["ssn"] = 3
# lecturer_service.create_lecturer(lecturer_data1)
# lecturer_service.create_lecturer(lecturer_data2)
# lecturer_service.create_lecturer(lecturer_data3)


# student_service.enroll_to_course(1, "B1")
# student_service.enroll_to_course(1, "B2")
# student_service.enroll_to_course(2, "B1")
# student_service.enroll_to_course(3, "B1")
# student_service.enroll_to_course(3, "B2")
# student_service.enroll_to_course(3, "B3")
# course_service.get_enrolled_students("B1")
# student_service.course_deregister(3, 2)
# student_service = StudentService(db_session)
#
# st = student_service.get_courses(3)
# print("-------------------------------------------")
# for s in st:
#     print(s.name)
# student_service.course_deregister(1, 2)
# student_service.get_student_course_table(1, 1)

# course_service = CourseService(db_session)
# lec = course_service.get_lecturer("B1")
# print("lec: {}\nname: {}\ncode: {}".format(lec, lec.name, lec.surname))
# course_service.assign_lecturer("B1", 1)