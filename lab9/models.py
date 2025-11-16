"""
Модели данных для SQLAlchemy
Часть 1: Создание моделей Users и Posts
"""

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    """
    Модель пользователя
    Таблица Users с полями:
    - id (целое число, первичный ключ, автоинкремент)
    - username (строка, уникальное значение)
    - email (строка, уникальное значение)
    - password (строка)
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)

    # Связь с постами (один ко многим)
    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"


class Post(Base):
    """
    Модель поста
    Таблица Posts с полями:
    - id (целое число, первичный ключ, автоинкремент)
    - title (строка)
    - content (текст)
    - user_id (целое число, внешний ключ, ссылающийся на поле id таблицы Users)
    """
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Связь с пользователем (многие к одному)
    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}', user_id={self.user_id})>"
