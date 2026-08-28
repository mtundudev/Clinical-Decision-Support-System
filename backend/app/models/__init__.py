#import your model here

from app.core.database import Base
from app.models.patient import Patient
from app.models.pathogen import Pathogen



__all__=["Base","Patient","Pathogen"]