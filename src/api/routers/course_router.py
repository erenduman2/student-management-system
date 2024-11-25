from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from src.database import db_session
from src.services import CourseService

from ..schemas import Course, LecturerCourse

router = APIRouter(prefix="/course")

course_service = CourseService(db_session)

@router.post("/create_course")
def create_course(course: Course):
    course_data = dict()
    course_data['name'] = course.name
    course_data['code'] = course.code
    course_data['credit'] = course.credit
    course_data['quota'] = course.quota
    ret = course_service.create_course(course_data)

    if not ret:
        raise HTTPException(status_code=409, detail="Course already exists..")

    return {
        "status": "success",
        "message": "Course created successfully",
        "data": course_data
    }

@router.delete("/delete_course/{course_code}")
def delete_course(course_code: str):
    # FIXME: Her tarafta ssn'leri id olarak değiştir.
    res = course_service.delete_course(course_code)

    if not res:
        raise HTTPException(status_code=404, detail="Course does not exist.")

    return {
        "status": "success",
        "message": "Course {} deleted successfully".format(course_code)
    }

@router.put("/assign_lecturer")
def assign_lecturer(lecturer_course: LecturerCourse):
    res = course_service.assign_lecturer(lecturer_course.course_code, lecturer_course.lecturer_id)
    if res:
        return {
            "status": "success",
            "message": "Lecturer is assigned to the course."
        }
    else:
        raise HTTPException(status_code=409, detail="Lecturer or Course does not exist.")

@router.get("/get_lecturer/{course_code}")
def get_lecturer(course_code: str):
    res = course_service.get_lecturer(course_code)
    if not res:
        raise HTTPException(status_code=409, detail="Student or Course does not exist.")
    return {
        "status": "success",
        "lecturer": res
    }

@router.put("/update_course")
def update_course(course: Course):
    ret = course_service.update_course(course.name, course.code, course.credit, course.quota)
    if not ret:
        raise HTTPException(status_code=409, detail="Course does not exist.")
    return {
        "status": "success",
        "message": "Course updated successfully",
    }

@router.get("/get_enrolled_students/{course_code}")
def get_enrolled_students(course_code: str):
    res = course_service.get_enrolled_students(course_code)
    if not res:
        raise HTTPException(status_code=409, detail="There is no course or enrolled students.")

    return {
        "status": "success",
        "enrolled_students": res
    }

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print("There is a problem.")
#     return JSONResponse(
#         status_code=422,
#         content={"message": "Veri doğrulama hatası!", "errors": exc.errors()},
#     )
