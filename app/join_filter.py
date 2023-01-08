from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *

Session = sessionmaker(bind = engine)
session = Session()


result = session.query(Student,Course).filter(studentcourse.student_id==Student.id,studentcourse.course_id==Course.id).filter(Course.id==3).all()
for row in result:
  print ("Name: ",row.Student.First_name,row.Student.Last_name)