from sqlalchemy.orm import sessionmaker

from db_create import engine
from models import *


Session = sessionmaker(bind = engine) #binds the db
session = Session()


    
    
discrete=Course(Course_name="Discrete Structure")
network =Course(Course_name="Computer Network")
ml=Course(Course_name="Machine Learning")
oop=Course(Course_name="Object-Oriented Design")
web=Course(Course_name="Web Development")
os=Course(Course_name="Operating System")
session.add_all([discrete,network,ml,oop,web,os])
session.commit()

oakton=School("Oakton College")
neui= School("NEUI")
uic= School("UIC")

John=Student(First_name='John',Last_name='Mathew')
John.Courses.append(ml)
John.Courses.append(network)

Jims=Student(First_name='Jims',Last_name='Publius')
Jims.Courses.append(os)

Jim = Student(First_name='Jim',Last_name='Gordon')
Jim.Courses.append(web)
Jim.Courses.append(os)

Sony = Student(First_name='Sony',Last_name='sebastian')
Sony.Courses.append(oop)
Sony.Courses.append(ml)

Raj = Student(First_name='Raj',Last_name='Mano')
Raj.Courses.append(web)
Raj.Courses.append(ml)

Lucy = Student(First_name='Lucy',Last_name='Manning')
Lucy.Courses.append(discrete)
Lucy.Courses.append(network)

Jack = Student(First_name='Jack',Last_name='London')
Jack.Courses.append(discrete)
Jack.Courses.append(network)




neui.Students = [Jim,Sony,Jack]
oakton.Students=[John,Jims]
uic.Students = [Lucy,Raj]

session.add(neui)
session.add(oakton)
session.add(uic)


session.add(Jim)
session.add(Sony)
session.add(Jack)
session.add(Lucy)
session.add(Raj)
session.add(Jims)
session.add(John)

session.commit()