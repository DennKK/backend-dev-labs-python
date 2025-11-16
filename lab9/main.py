"""
Веб-приложение FastAPI с интеграцией SQLAlchemy
Часть 3: Базовые операции с базой данных в веб-приложении
"""

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import crud
import models
import schemas
from database import engine, get_db, create_tables

# Создание таблиц при запуске приложения
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lab 9 - SQLAlchemy Integration",
    description="FastAPI приложение с базой данных для управления пользователями и постами",
    version="1.0.0"
)


@app.get("/")
async def root():
    """
    Главная страница API
    """
    return {
        "message": "Lab 9 - SQLAlchemy Integration API",
        "docs": "/docs",
        "endpoints": {
            "users": "/users",
            "posts": "/posts"
        }
    }


# ========== Endpoints для User ==========

@app.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Создание нового пользователя
    Часть 3: CRUD операция - Create (User)
    """
    # Проверка на уникальность username
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username уже зарегистрирован")
    
    # Проверка на уникальность email
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")
    
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка всех пользователей
    Часть 3: CRUD операция - Read (Users)
    """
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.UserWithPosts)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Получение информации о конкретном пользователе с его постами
    Часть 3: CRUD операция - Read (User)
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    """
    Обновление данных пользователя
    Часть 3: CRUD операция - Update (User)
    """
    db_user = crud.update_user(db, user_id=user_id, user_update=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Удаление пользователя и всех его постов
    Часть 3: CRUD операция - Delete (User)
    """
    success = crud.delete_user(db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return None


# ========== Endpoints для Post ==========

@app.post("/posts/", response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    """
    Создание нового поста
    Часть 3: CRUD операция - Create (Post)
    """
    # Проверка существования пользователя
    db_user = crud.get_user(db, user_id=post.user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    return crud.create_post(db=db, post=post)


@app.get("/posts/", response_model=List[schemas.PostWithUser])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка всех постов с информацией об авторах
    Часть 3: CRUD операция - Read (Posts)
    """
    posts = crud.get_posts_with_users(db, skip=skip, limit=limit)
    return posts


@app.get("/posts/{post_id}", response_model=schemas.PostWithUser)
def read_post(post_id: int, db: Session = Depends(get_db)):
    """
    Получение информации о конкретном посте
    Часть 3: CRUD операция - Read (Post)
    """
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Пост не найден")
    return db_post


@app.get("/users/{user_id}/posts/", response_model=List[schemas.Post])
def read_user_posts(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение всех постов конкретного пользователя
    Часть 3: CRUD операция - Read (User Posts)
    """
    # Проверка существования пользователя
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    posts = crud.get_posts_by_user(db, user_id=user_id, skip=skip, limit=limit)
    return posts


@app.put("/posts/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, post: schemas.PostUpdate, db: Session = Depends(get_db)):
    """
    Обновление поста
    Часть 3: CRUD операция - Update (Post)
    """
    db_post = crud.update_post(db, post_id=post_id, post_update=post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Пост не найден")
    return db_post


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    """
    Удаление поста
    Часть 3: CRUD операция - Delete (Post)
    """
    success = crud.delete_post(db, post_id=post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Пост не найден")
    return None
