from typing import Union
from fastapi import FastAPI, APIRouter
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from src.database import db_session
from src.services import LecturerService
# app = FastAPI()
router = APIRouter(prefix="/lecturer")

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
class Course(BaseModel):
    name: str
    code: str
    credit: int
    quota: int
class Student(BaseModel):
    name: str
    surname: str
    ssn: str
class Lecturer(BaseModel):
    name: str
    surname: str
    ssn: str
class StudentCourse(BaseModel):
    student_ssn: str
    course_code: str
class LecturerCourse(BaseModel):
    lecturer_id: int
    course_code: str

lecturer_service = LecturerService(db_session)

@router.post("/create_lecturer")
def create_lecturer(lecturer: Lecturer):
    lecturer_data = dict()
    lecturer_data['name'] = lecturer.name
    lecturer_data['surname'] = lecturer.surname
    lecturer_data['ssn'] = lecturer.ssn
    ret = lecturer_service.create_lecturer(lecturer_data)

    if not ret:
        raise HTTPException(status_code=409, detail="Lecturer already exists..")

    return {
        "status": "success",
        "message": "Lecturer created successfully",
        "data": lecturer_data
    }

@router.delete("/delete_lecturer/{lecturer_ssn}")
def delete_lecturer(lecturer_ssn: str):
    # FIXME: Her tarafta ssn'leri id olarak değiştir.
    res = lecturer_service.delete_lecturer(lecturer_ssn)

    if not res:
        raise HTTPException(status_code=404, detail="Lecturer does not exist.")

    return {
        "status": "success",
        "message": "Lecturer {} deleted successfully".format(lecturer_ssn)
    }

@router.put("/add_course")
def add_course(lecturer_course: LecturerCourse):
    res = lecturer_service.add_course(lecturer_course.course_code, lecturer_course.lecturer_id)
    if res:
        return {
            "status": "success",
            "message": "Lecturer is assigned to the course."
        }
    else:
        raise HTTPException(status_code=409, detail="Lecturer or Course does not exist.")

@router.get("/get_courses/{lecturer_id}")
def get_courses(lecturer_id: int):
    res = lecturer_service.get_courses(lecturer_id)
    if not res:
        raise HTTPException(status_code=409, detail="Student or Course does not exist.")
    return {
        "status": "success",
        "courses": res
    }

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print("There is a problem.")
#     return JSONResponse(
#         status_code=422,
#         content={"message": "Veri doğrulama hatası!", "errors": exc.errors()},
#     )
