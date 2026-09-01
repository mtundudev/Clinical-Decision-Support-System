from fastapi import APIRouter,Depends
from app.core.database import get_db
from typing import List
from sqlalchemy.orm import Session
from app.services.patient import PatientServices
from app.schemas.patient import PatientCreate,PatientUpdate,PatientResponse

router=APIRouter(prefix="/patient",tags=["Patient"])

@router.post("/register",response_model=PatientResponse)
def register(data:PatientCreate,db:Session=Depends(get_db)):
    return PatientServices.register_patient(data,db)

@router.get("",response_model=List[PatientResponse])
def show(db:Session=Depends(get_db)):
    return PatientServices.retrieve_patients(db)

@router.get("/{patient_id}",response_model=PatientResponse)
def showbyid(patient_id:int,db:Session=Depends(get_db)):
    return PatientServices.retrieve_id(patient_id,db)


@router.patch("/{patient_id}",response_model=PatientResponse)
def discharge(patient_id:int,db:Session=Depends(get_db)):
    return PatientServices.discharge_patient(patient_id,db)

@router.put("/{patient_id}",response_model=PatientResponse)
def modufy(patient_id:int,data:PatientUpdate,db:Session=Depends(get_db)):
    return PatientServices.update_patient_info(patient_id,data,db)

@router.delete("/{patient_id}")
def delete(patient_id:int,db:Session=Depends(get_db)):
    return PatientServices.delete_patient(patient_id,db)