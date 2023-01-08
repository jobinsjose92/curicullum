from db_create import Base
from sqlalchemy import Column, Integer, String,ForeignKey,Table
from sqlalchemy.orm import relationship


class studentcourse(Base):
  __tablename__ = "association_table"
  course_id=Column(Integer(), ForeignKey("courses.id"),primary_key=True)
  student_id=Column(Integer(), ForeignKey("students.id"),primary_key=True)


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer(), primary_key=True)
    Course_name = Column(String(30), nullable=False)
  
    def __init__(self,Course_name):
       self.Course_name=Course_name
    def __repr__(self):
        return "Course Name='%s'"%(self.Course_name)


class Student(Base):
     __tablename__ = "students"
     id = Column(Integer, primary_key=True)
     First_name = Column(String(30), nullable=False)
     Last_name = Column(String(30), nullable=False)
     school_id = Column(Integer(), ForeignKey('schools.School_id') )
     Courses  = relationship("Course",secondary="association_table", backref="students")
     school = relationship("School", back_populates="Students")

     def __init__(self,First_name, Last_name):
         self.First_name=First_name
         self.Last_name=Last_name
         

     def __repr__(self):
        return "Student Name='%s''%s'"%(self.First_name,self.Last_name)




class School(Base):
    __tablename__ = "schools"
    School_id = Column(Integer(), primary_key=True)
    School_name = Column(String(30), nullable=False)
    Students   = relationship("Student",back_populates="school")
    Students  = relationship("Student", back_populates='school',cascade="all, delete, delete-orphan")
    def __init__(self,School_name ):
        self.School_name=School_name

    def __repr__(self):
        return "School Name='%s'"%(self.School_name)


#School.students = relationship(
 #  "Student", order_by=Student.id, back_populates="user")

"""
class studentCourse(Base):
        __tablename__ = 'studentcourse'
        course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
        student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
        def __init__(self,courses):
         self.courses=courses
        courses = relationship(Course,lazy='joined')
"""

