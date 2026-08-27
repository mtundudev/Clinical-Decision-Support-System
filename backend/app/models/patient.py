from app.core.database import Base
from sqlalchemy import Column,String,Integer,DateTime,Date
from datetime import datetime,date

class Patient(Base):
    __tablename__="patients"
    id=Column(Integer,primary_key=True)
    full_name=Column(String,nullable=True)
    patient_code=Column(String,nullable=True,unique=True)
    date_of_birth=Column(Date,nullable=False)
    age=Column(Integer,nullable=True)
    sex=Column(String,nullable=False)
    ward=Column(String,nullable=True)
    admission_date=Column(Date,default=date.today)
    discharged_date=Column(Date)
    
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)