from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.core.database import Base


class Pathogen(Base):
    __tablename__ = "pathogens"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, unique=True, index=True)
    scientific_name = Column(String(200), nullable=True)
    gram_stain = Column(String(20), nullable=True)   # "Positive" / "Negative"
    category = Column(String(100), nullable=True)    # e.g. Bacteria, Fungi, Virus
    description = Column(Text, nullable=True)

    created_at = Column(DateTime,default=datetime.now)
    updated_at = Column(DateTime,default=datetime.now, onupdate=datetime.now())