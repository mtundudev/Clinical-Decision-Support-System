from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.pathogen import PathogenCreate, PathogenUpdate, PathogenResponse
from app.services.pathogens import PathogenServices

router = APIRouter(prefix="/pathogens", tags=["Pathogens"])


@router.post("/", response_model=PathogenResponse, status_code=201)
def create_pathogen(data: PathogenCreate, db: Session = Depends(get_db)):
    return PathogenServices.create_pathogen(db, data)


@router.get("/", response_model=list[PathogenResponse])
def list_pathogens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return PathogenServices.get_pathogens(db, skip, limit)


@router.get("/{pathogen_id}", response_model=PathogenResponse)
def get_pathogen(pathogen_id: int, db: Session = Depends(get_db)):
    return PathogenServices.get_pathogen_by_id(db, pathogen_id)


@router.put("/{pathogen_id}", response_model=PathogenResponse)
def update_pathogen(pathogen_id: int, data: PathogenUpdate, db: Session = Depends(get_db)):
    return PathogenServices.update_pathogen(db, pathogen_id, data)


@router.delete("/{pathogen_id}", status_code=204)
def delete_pathogen(pathogen_id: int, db: Session = Depends(get_db)):
    return PathogenServices.delete_pathogen(db, pathogen_id)