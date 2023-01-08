from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *

Session = sessionmaker(bind = engine)
session = Session()



result = session.query(Student,Course).filter(studentcourse.student_id==Student.id,studentcourse.course_id==Course.id).filter(Course.id==4).all()
for row in result:
  print ("Name: ",row.Student.First_name)


courses= session.query(Course, Student).filter(studentcourse.student_id==Student.id,studentcourse.course_id==Course.id).filter(Student.id==1).all()
for orderitem in courses:
    print(orderitem.Course.Course_name)

school = session.query(School).all()

for x in school:
  print("student",x.Students)