from pydantic import BaseModel

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
    lecturer_ssn: str
    course_code: str
