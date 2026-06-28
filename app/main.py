from fastapi import FastAPI
from app.api import books, categories

app = FastAPI(
    title="Book Library API",
    description="API для управления библиотекой книг",
    version="1.0.0"
)

app.include_router(categories.router)
app.include_router(books.router)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "API is running"}

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Book Library API",
        "docs": "/docs",
        "health": "/health"
    }