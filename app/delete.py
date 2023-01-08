from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *

Session = sessionmaker(bind = engine)
session = Session()

jim = session.query(Student).filter(Student.First_name == "Jim").first()
session.delete(jim)
session.commit()


uic = session.query(School).filter(School.School_id == 3).first()
session.delete(uic)
session.commit()