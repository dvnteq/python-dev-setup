from sqlalchemy.orm import Session
from . import models

# Category CRUD (Create, Read, Update, Delete)

# Create
def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Read
def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

# Update
def update_category(db: Session, category_id: int, new_title: str):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db_category.title = new_title
        db.commit()
        db.refresh(db_category)
    return db_category

# Delete
def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category


# Book CRUD (Create, Read, Update, Delete)

# Create
def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    db_book = models.Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Read
def get_books(db: Session):
    return db.query(models.Book).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

# Update
def update_book(db: Session, book_id: int, title: str = None, price: float = None):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        if title is not None:
            db_book.title = title
        if price is not None:
            db_book.price = price
        db.commit()
        db.refresh(db_book)
    return db_book

# Delete
def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book