#import your model here

from app.core.database import Base
from app.models.patient import Patient
from app.models.antibiotic import Antibiotic



__all__=["Base","Patient","Antibiotic"]