from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class AntibioticBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    class_name: Optional[str] = None
    route: Optional[str] = None
    description: Optional[str] = None


class AntibioticCreate(AntibioticBase):
    pass


class AntibioticUpdate(BaseModel):
    name: Optional[str] = None
    class_name: Optional[str] = None
    route: Optional[str] = None
    description: Optional[str] = None


class AntibioticResponse(AntibioticBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}