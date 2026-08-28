from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException,status
from app.models.antibiotic import Antibiotic
from app.schemas.antibiotic import AntibioticCreate, AntibioticUpdate

class AntibioticServices():
    @staticmethod
    def create_antibiotic(db: Session, data: AntibioticCreate):
        antibiotic = Antibiotic(
            name=data.name,
            class_name=data.class_name,
            route=data.route,
            description=data.description
        )
        db.add(antibiotic)
        try:
            db.commit()
            db.refresh(antibiotic)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="antibiotic already created")
        return antibiotic

    @staticmethod
    def get_antibiotics(db: Session):       
        return db.query(Antibiotic).all()

    @staticmethod
    def get_antibiotic_by_id(db: Session, antibiotic_id: int) -> Antibiotic:        
        antibiotic = db.query(Antibiotic).filter(Antibiotic.id == antibiotic_id).first()
        if not antibiotic:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")
        return antibiotic

    @staticmethod
    def update_antibiotic(db: Session, antibiotic_id: int, data: AntibioticUpdate) -> Antibiotic:       
        antibiotic = db.query(Antibiotic).filter(Antibiotic.id == antibiotic_id).first()
        if not antibiotic:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")
        antibiotic.name=data.name
        antibiotic.class_name=data.class_name
        antibiotic.route=data.route
        antibiotic.description=data.description
       
        db.commit()
        db.refresh(antibiotic)
        return antibiotic

    @staticmethod
    def delete_antibiotic(db: Session, antibiotic_id: int) -> None:
        antibiotic = db.query(Antibiotic).filter(Antibiotic.id == antibiotic_id).first()
        if not antibiotic:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")
        db.delete(antibiotic)
        db.commit()
        return {
            "message":"deleted succesful"
        }  