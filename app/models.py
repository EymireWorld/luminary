from datetime import datetime

from sqlalchemy import ARRAY as Array
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column
)


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr 
    def __tablename__(cls):
        return f'{cls.__name__.lower()}s'
    
    id: Mapped[int] = mapped_column(primary_key= True, index= True)


class User(Base):
    username: Mapped[str] = mapped_column(unique= True, index= True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique= True)
    hashed_password: Mapped[bytes]
    created_at: Mapped[datetime]


class Post(Base):
    description: Mapped[str | None] = mapped_column(String(256), default= None)
    filename: Mapped[str]
    likes: Mapped[list[int]] = mapped_column(Array(Integer))
    created_at: Mapped[datetime]


class Comment(Base):
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'), index= True)
    text: Mapped[str] = mapped_column(String(256))
    created_at: Mapped[datetime]
    edited_at: Mapped[datetime | None] = mapped_column(default= None)
