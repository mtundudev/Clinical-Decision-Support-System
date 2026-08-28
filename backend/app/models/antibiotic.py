from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime 
from app.core.database import Base


class Antibiotic(Base):
    __tablename__ = "antibiotics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, unique=True, index=True)
    class_name = Column(String(150), nullable=True)   # e.g. Penicillin, Cephalosporin
    route = Column(String(50), nullable=True)          # e.g. Oral, IV, IM
    description = Column(Text, nullable=True)

    created_at = Column(DateTime,default=datetime.now)
    updated_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)