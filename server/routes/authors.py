from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.author import Author as AuthorSchema
from models.author import Author as AuthorModel
from config.db_setup import get_db

router = APIRouter()

@router.post('/add-author', response_model=AuthorSchema)
def add_author(author: AuthorSchema, db: Session = Depends(get_db)):
    db_author = AuthorModel(name=author.name, age=author.age)
    db.add(db_author)
    db.commit()
    return db_author
