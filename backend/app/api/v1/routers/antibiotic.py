from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.antibiotic import AntibioticCreate, AntibioticUpdate, AntibioticResponse
from app.services.antibiotic import AntibioticServices

router = APIRouter(prefix="/antibiotics", tags=["Antibiotics"])


@router.post("/", response_model=AntibioticResponse, status_code=201)
def create_antibiotic(data: AntibioticCreate, db: Session = Depends(get_db)):
    return AntibioticServices.create_antibiotic(db, data)


@router.get("/", response_model=list[AntibioticResponse])
def list_antibiotics(db: Session = Depends(get_db)):
    return AntibioticServices.get_antibiotics(db)


@router.get("/{antibiotic_id}", response_model=AntibioticResponse)
def get_antibiotic(antibiotic_id: int, db: Session = Depends(get_db)):
    return AntibioticServices.get_antibiotic_by_id(db, antibiotic_id)


@router.put("/{antibiotic_id}", response_model=AntibioticResponse)
def update_antibiotic(antibiotic_id: int, data: AntibioticUpdate, db: Session = Depends(get_db)):
    return AntibioticServices.update_antibiotic(db, antibiotic_id, data)


@router.delete("/{antibiotic_id}")
def delete_antibiotic(antibiotic_id: int, db: Session = Depends(get_db)):
    return  AntibioticServices.delete_antibiotic(db, antibiotic_id)