from pydantic import BaseModel,Field,field_validator
from typing import Optional
from datetime import datetime,date


class PatientCreate(BaseModel):
    full_name:Optional[str]=None
    date_of_birth:date
    sex:str
    ward:Optional[str]=None
    
    @field_validator("date_of_birth")
    @staticmethod
    def dob(cls,value):
        if value > date.today():
            raise ValueError("invalid,please check your dob")
        return value
    
class PatientUpdate(BaseModel):
    full_name:Optional[str]=None
    date_of_birth:Optional[date]=None
    sex:Optional[str]=None
    ward:Optional[str]=None

class PatientResponse(BaseModel):
          
    id:int
    full_name:str
    patient_code:str
    age:int
    date_of_birth:date
    sex:str
    ward:str
    admission_date:date
    discharged_date:Optional[date]=None
    created_at:datetime
    updated_at:datetime
        

    