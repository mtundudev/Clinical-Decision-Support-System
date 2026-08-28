from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException,status
from app.models.pathogen import Pathogen
from app.schemas.pathogen import PathogenCreate, PathogenUpdate


class PathogenServices():
    @staticmethod
    def create_pathogen(db: Session, data: PathogenCreate):
        pathogen = Pathogen(
            name=data.name,
            scientific_name=data.scientific_name,
            gram_stain=data.gram_stain,
            category=data.category,
            description=data.description
        )
        db.add(pathogen)
        try:
            db.commit()         
            db.refresh(pathogen)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="pathogen wth this unfo already exist")
        return pathogen




    @staticmethod
    def get_pathogens(db: Session):
        pathogen= db.query(Pathogen).all()
        return pathogen

    @staticmethod
    def get_pathogen_by_id(db: Session, pathogen_id: int):
        pathogen = db.query(Pathogen).filter(Pathogen.id == pathogen_id).first()
        if not pathogen:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="pathogen not found")
        return pathogen

    @staticmethod
    def update_pathogen(db: Session, pathogen_id: int, data: PathogenUpdate):
        pathogen = db.query(Pathogen).filter(Pathogen.id == pathogen_id).first()
        if not pathogen:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="pathogen not found")
    
        pathogen.name=data.name
        pathogen.scientific_name=data.scientific_name
        pathogen.gram_stain=data.gram_stain
        pathogen.category=data.category
        pathogen.description=data.description

    
        db.commit()
        db.refresh(pathogen)
        return pathogen

    @staticmethod
    def delete_pathogen(db: Session, pathogen_id: int) :
        pathogen = db.query(Pathogen).filter(Pathogen.id == pathogen_id).first()
        if not pathogen:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="pathogen not found")
    
        db.delete(pathogen)
        db.commit()
    
        return {
            "message":" pathogen deleted succesful"
        }

