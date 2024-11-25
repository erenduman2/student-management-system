from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from src.database import db_session
from src.services import StudentService

from ..schemas import Student, StudentCourse

router = APIRouter(prefix="/student")

student_service = StudentService(db_session)

@router.post("/create_student")
def create_student(student: Student):
    student_data = dict()
    student_data['name'] = student.name
    student_data['surname'] = student.surname
    student_data['ssn'] = student.ssn
    ret = student_service.create_student(student_data)
    if ret:
        print("API MESAJI: Ogrenci OLDU")
    else:
        raise HTTPException(status_code=409, detail="Student already exists..")
        # print("API MESAJI: Ogrenci OLMADI")

    return {
        "status": "success",
        "message": "Student created successfully",
        "data": student_data
    }

@router.delete("/delete_student/{student_id}")
def delete_student(student_id: str):
    # FIXME: Her tarafta ssn'leri id olarak değiştir.
    student_ssn = student_id
    res = student_service.delete_student(student_ssn)

    if not res:
        raise HTTPException(status_code=404, detail="Student does not exist.")

    return {
        "status": "success",
        "message": "Student {} deleted successfully".format(student_ssn)
    }

@router.post("/enroll_to_course")
def enroll_to_course(student_course: StudentCourse):
    res = student_service.enroll_to_course(student_course.student_ssn, student_course.course_code)
    if res:
        return {
            "status": "success",
            "message": "Student is enrolled to the course."
        }
    else:
        raise HTTPException(status_code=409, detail="Student or Course does not exist.")

@router.delete("/course_deregister")
def course_deregister(student_course: StudentCourse):
    res = student_service.course_deregister(student_course.student_ssn, student_course.course_code)
    if not res:
        raise HTTPException(status_code=409, detail="Student or Course does not exist.")
    return {
        "status": "success",
        "message": "Student is deregistered successfully."
    }
@router.get("/get_courses")
def get_courses(student_ssn: str):
    courses = student_service.get_courses(student_ssn)
    return courses



# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print("There is a problem.")
#     return JSONResponse(
#         status_code=422,
#         content={"message": "Veri doğrulama hatası!", "errors": exc.errors()},
#     )
