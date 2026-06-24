from app.db import SessionLocal
from app.db import crud

db = SessionLocal()

print("\nКатегории книг:\n")

categories = crud.get_categories(db)
for category in categories:
    print(f"ID: {category.id} - Название: {category.title}")

print("\nСПИСОК КНИГ\n")

books = crud.get_books(db)
for book in books:
    print(f"ID: {book.id}")
    print(f"Название: {book.title}")
    print(f"Описание: {book.description}")
    print(f"Цена: {book.price} руб.")
    print(f"Категория ID: {book.category_id}")
    print("\n")

db.close()