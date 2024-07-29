from pydantic import BaseModel
from pydantic import BaseModel
from typing import Optional
from app.schemas.category import CategoryResponse

class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    category_id: Optional[int] = None

class QuestionResponse(QuestionBase):
    id: int
    text: str
    category: Optional[CategoryResponse]

    class Config:
        orm_mode: True