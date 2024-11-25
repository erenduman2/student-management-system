from sqlalchemy import Table, Column
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


student_course = Table(
    'student_course',
    Base.metadata,
    Column("student_id", ForeignKey("student.id"), primary_key=True),
    Column("course_id", ForeignKey("course.id"), primary_key=True),
)

class Student(Base):
    __tablename__ = 'student'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) # auto olmayacak
    name: Mapped[str]
    surname: Mapped[str]
    ssn: Mapped[str] = mapped_column(unique=True)
    gender: Mapped[str] = mapped_column(nullable=True)
    birth_date = mapped_column(DateTime, nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    credit_count: Mapped[int] = mapped_column(default=0)
    active_credit_count: Mapped[int] = mapped_column(default=0)
    max_active_credit: Mapped[int] = mapped_column(default=25)
    enrolled_courses: Mapped[list["Course"]] = relationship(secondary=student_course, back_populates='enrolled_students')
    # courses: Mapped[list[Course]] = mapped_column(nullable=False)

class Course(Base):
    __tablename__ = 'course'
    id: Mapped[int] = mapped_column(primary_key=True)
    lecturer_id: Mapped[int] = mapped_column(ForeignKey('lecturer.id'), nullable=True)
    code: Mapped[str] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(40))
    credit: Mapped[int]
    quota: Mapped[int] = mapped_column(nullable=True)
    student_count: Mapped[int] = mapped_column(default=0)
    lecturer: Mapped["Lecturer"] = relationship(back_populates="given_courses")
    enrolled_students: Mapped[list["Student"]] = relationship(secondary=student_course, back_populates='enrolled_courses')

class Lecturer(Base):
    __tablename__ = 'lecturer'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    ssn: Mapped[str] = mapped_column(nullable=False, unique=True)
    birth_date: Mapped[str] = mapped_column(DateTime, nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    given_courses: Mapped[list["Course"]] = relationship(back_populates="lecturer")