from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.book import Book as BookSchema
from models.book import Book as BookModel
from config.db_setup import get_db

router = APIRouter()

@router.post('/add-book', response_model=BookSchema)
def add_book( book: BookSchema, db: Session = Depends(get_db)):
    db_book = BookModel(title=book.title, rating=book.rating, author_id=book.author.id)
    db.add(db_book)
    db.commit()
    return db_book
