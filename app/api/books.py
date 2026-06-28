from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])

# Получить все книги (с опциональной фильтрацией по категории)
@router.get("/", response_model=List[schemas.BookResponse])
def get_books(
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    db: Session = Depends(get_db)
):
    if category_id:
        # Проверяем существование категории
        category = crud.get_category(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        # Получаем книги конкретной категории
        books = crud.get_books(db)
        return [book for book in books if book.category_id == category_id]
    return crud.get_books(db)

# Получить книгу по ID
@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Создать книгу
@router.post("/", response_model=schemas.BookResponse, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # Проверяем существование категории
    category = crud.get_category(db, book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return crud.create_book(
        db,
        title=book.title,
        description=book.description,
        price=book.price,
        url=book.url,
        category_id=book.category_id
    )

# Обновить книгу
@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    # Проверяем существование книги
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Если указана новая категория, проверяем её существование
    if book.category_id:
        category = crud.get_category(db, book.category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
    
    return crud.update_book(
        db,
        book_id=book_id,
        title=book.title,
        price=book.price
    )

# Удалить книгу
@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}