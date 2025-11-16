"""
Pydantic схемы для валидации данных
Используются для валидации входящих и исходящих данных через API
"""

from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional


# ========== Схемы для User ==========

class UserBase(BaseModel):
    """Базовая схема пользователя"""
    username: str = Field(..., min_length=3, max_length=50, description="Имя пользователя")
    email: EmailStr = Field(..., description="Email адрес")


class UserCreate(UserBase):
    """Схема для создания пользователя"""
    password: str = Field(..., min_length=6, max_length=255, description="Пароль")


class UserUpdate(BaseModel):
    """Схема для обновления пользователя"""
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6, max_length=255)


class User(UserBase):
    """Схема пользователя для ответа"""
    id: int
    
    class Config:
        from_attributes = True  # Позволяет работать с ORM объектами


class UserWithPosts(User):
    """Схема пользователя с его постами"""
    posts: List['Post'] = []
    
    class Config:
        from_attributes = True


# ========== Схемы для Post ==========

class PostBase(BaseModel):
    """Базовая схема поста"""
    title: str = Field(..., min_length=1, max_length=200, description="Заголовок поста")
    content: str = Field(..., min_length=1, description="Содержание поста")


class PostCreate(PostBase):
    """Схема для создания поста"""
    user_id: int = Field(..., gt=0, description="ID пользователя-автора")


class PostUpdate(BaseModel):
    """Схема для обновления поста"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1)


class Post(PostBase):
    """Схема поста для ответа"""
    id: int
    user_id: int
    
    class Config:
        from_attributes = True


class PostWithUser(Post):
    """Схема поста с информацией об авторе"""
    user: User
    
    class Config:
        from_attributes = True
