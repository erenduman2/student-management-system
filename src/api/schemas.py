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

