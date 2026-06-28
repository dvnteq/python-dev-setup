from pydantic import BaseModel
from typing import Optional, List

# Category Schemas

class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    title: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int
    
    class Config:
        from_attributes = True


# Book Schemas

class BookBase(BaseModel):
    title: str
    description: str
    price: float
    url: Optional[str] = None
    category_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookResponse(BookBase):
    id: int
    
    class Config:
        from_attributes = True

class BookWithCategory(BookResponse):
    category: Optional[CategoryResponse] = None