from app.schemas.patient import PatientCreate,PatientUpdate
from sqlalchemy.orm import Session
from app.models.patient import Patient
from datetime import datetime,date
from fastapi import HTTPException,status

class PatientServices():
    @staticmethod
    def auto_patient_code(patient_id:int):
        year_name=datetime.now().year
        return f"PAT-{year_name}-{patient_id:06d}"
    @staticmethod
    def calculate_age(dob:date):
        today=date.today()    
        return today.year - dob.year-((today.month, today.day)<(dob.month ,dob.day))
    @staticmethod
    def register_patient(data:PatientCreate,db:Session):
        patient=Patient(
            full_name=data.full_name,
            date_of_birth=data.date_of_birth,
            age=PatientServices.calculate_age(data.date_of_birth),
            sex=data.sex,
            ward=data.ward
            
        )
        
        db.add(patient)
        db.flush()
        patient.patient_code=PatientServices.auto_patient_code(patient.id)
        db.commit()
        db.refresh(patient)
        
        
        return patient
    
    @staticmethod
    def retrieve_patients(db:Session):
        patient=db.query(Patient).all()
        return patient
    
    @staticmethod
    def retrieve_id(patient_id:int,db:Session):
        patient=db.query(Patient).filter(Patient.id==patient_id).first()
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="patient not found")
        
        return patient
    
    @staticmethod
    def discharge_patient(patient_id:int,db:Session):
        patient=db.query(Patient).filter(Patient.id==patient_id).first()
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="patient not found")
        patient.discharged_date=date.today()
        db.commit()
        db.refresh(patient)
        return patient
    
    @staticmethod
    def update_patient_info(patient_id:int,data:PatientUpdate,db:Session):
        patient=db.query(Patient).filter(Patient.id==patient_id).first()
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="patient not found")
        if data.full_name:
            patient.full_name=data.full_name
        if data.date_of_birth:
            patient.date_of_birth=data.date_of_birth
            patient.age=PatientServices.calculate_age(data.date_of_birth)
        if data.sex:
            patient.sex=data.sex
        if data.ward:
            patient.ward==data.ward   
            
        db.commit()             
        db.refresh(patient)
        
        return patient
    
    @staticmethod
    def delete_patient(patient_id,db:Session):
        patient=db.query(Patient).filter(Patient.id==patient_id).first()
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="patient not found")
        
        db.delete(patient)
        db.commit()
        return {
            "message":"patient information deleted succesfuly"
        }