from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class PathogenBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    scientific_name: Optional[str] = None
    gram_stain: Optional[str] = Field(None, pattern="^(Positive|Negative)$")
    category: Optional[str] = None
    description: Optional[str] = None


class PathogenCreate(PathogenBase):
    pass


class PathogenUpdate(BaseModel):
    name: Optional[str] = None
    scientific_name: Optional[str] = None
    gram_stain: Optional[str] = Field(None, pattern="^(Positive|Negative)$")
    category: Optional[str] = None
    description: Optional[str] = None


class PathogenResponse(PathogenBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}