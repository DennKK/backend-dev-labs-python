"""
Подключение к базе данных и настройка сессий
Часть 1: Подключение к базе данных
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./lab9_database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=True  # Включает логирование SQL запросов (для отладки)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Функция для получения сессии базы данных
    Используется как зависимость в FastAPI endpoints
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """
    Создание всех таблиц в базе данных
    """
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы!")


def drop_tables():
    """
    Удаление всех таблиц из базы данных
    """
    Base.metadata.drop_all(bind=engine)
    print("Таблицы успешно удалены!")
