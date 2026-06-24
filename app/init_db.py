from app.db import Base, engine
from app.db import crud
from app.db.db import SessionLocal

#Создаём таблицы в БД
Base.metadata.create_all(bind=engine)

db = SessionLocal()

#Добавляем категории
category1 = crud.create_category(db, title="Фантастика")
category2 = crud.create_category(db, title="Программирование")

print(f"Созданы категории: {category1.title}, {category2.title}")

#Добавляем книги к первой категории
crud.create_book(db, title="Дюна", description="Классика научной фантастики", price=599.99, url="", category_id=category1.id)
crud.create_book(db, title="Основание", description="Цикл Айзека Азимова", price=499.99, url="", category_id=category1.id)

#Добавляем книги ко второй категории
crud.create_book(db, title="Изучаем Python", description="Книга для начинающих программистов", price=899.99, url="", category_id=category2.id)
crud.create_book(db, title="Clean Code", description="Роберт Мартин — чистый код", price=1299.99, url="", category_id=category2.id)

db.close()

print("\nБаза данных успешно инициализирована!")
print("Добавлено 2 категории и 4 книги")