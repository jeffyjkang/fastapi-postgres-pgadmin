from pydantic import BaseModel
from models.book import Choices

class Book(BaseModel):
    title: str
    rating: Choices
    author_id: int
    class Config:
        orm_mode = True
