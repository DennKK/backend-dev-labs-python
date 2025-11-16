"""
CRUD операции для работы с базой данных
Часть 2: Взаимодействие с базой данных
"""

from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
import models
import schemas

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """
    Создание нового пользователя
    Часть 2: Добавление данных в таблицу Users
    """
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> Optional[models.User]:
    """
    Получение пользователя по ID
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    """
    Получение пользователя по имени
    """
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    """
    Получение пользователя по email
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    """
    Получение всех пользователей
    Часть 2: Извлечение всех записей из таблицы Users
    """
    return db.query(models.User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate) -> Optional[models.User]:
    """
    Обновление данных пользователя
    Часть 2: Обновление поля email у пользователя
    """
    db_user = get_user(db, user_id)
    if db_user is None:
        return None

    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> bool:
    """
    Удаление пользователя
    Часть 2: Удаление пользователя и всех его постов (каскадное удаление)
    """
    db_user = get_user(db, user_id)
    if db_user is None:
        return False
    
    db.delete(db_user)
    db.commit()
    return True


def create_post(db: Session, post: schemas.PostCreate) -> models.Post:
    """
    Создание нового поста
    Часть 2: Добавление данных в таблицу Posts
    """
    db_post = models.Post(
        title=post.title,
        content=post.content,
        user_id=post.user_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: int) -> Optional[models.Post]:
    """
    Получение поста по ID
    """
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100) -> List[models.Post]:
    """
    Получение всех постов
    Часть 2: Извлечение всех записей из таблицы Posts
    """
    return db.query(models.Post).offset(skip).limit(limit).all()


def get_posts_with_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.Post]:
    """
    Получение всех постов с информацией об авторах
    Часть 2: Извлечение всех записей из таблицы Posts, 
    включая информацию о пользователях, которые их создали
    """
    return db.query(models.Post).options(joinedload(models.Post.user)).offset(skip).limit(limit).all()


def get_posts_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[models.Post]:
    """
    Получение постов конкретного пользователя
    Часть 2: Извлечение записей из таблицы Posts, созданных конкретным пользователем
    """
    return db.query(models.Post).filter(models.Post.user_id == user_id).offset(skip).limit(limit).all()


def update_post(db: Session, post_id: int, post_update: schemas.PostUpdate) -> Optional[models.Post]:
    """
    Обновление поста
    Часть 2: Обновление поля content у поста
    """
    db_post = get_post(db, post_id)
    if db_post is None:
        return None
    
    # Обновляем только те поля, которые были переданы
    update_data = post_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_post, field, value)
    
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int) -> bool:
    """
    Удаление поста
    Часть 2: Удаление одного из постов
    """
    db_post = get_post(db, post_id)
    if db_post is None:
        return False
    
    db.delete(db_post)
    db.commit()
    return True
