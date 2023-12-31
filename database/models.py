from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Float, Date, Boolean, BigInteger, null
from sqlalchemy.orm import relationship
from database import Base

# таблица пользователей


class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    mail = Column(String, nullable=False)
    user_city = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    password = Column(String)
    reg_date = Column(DateTime)

# таблица постов


class UserPost(Base):
    __tablename__ = 'user_posts'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    main_text = Column(String, nullable=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')

# таблиц фото


class PostPhoto(Base):
    __tablename__ = 'post_photos'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    post_id = Column(BigInteger, ForeignKey("user_posts.id"))
    photo_path = Column(String, nullable=False)

    post_fk = relationship(UserPost, lazy='subquery')
# таблица коментов


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    post_id = Column(BigInteger, ForeignKey("user_posts.id"))
    text = Column(String, nullable=False, unique=True)
    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')
# таблица хэштегов


class Hashtags(Base):
    __tablename__ = 'hashtags'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    hashtag = Column(String, nullable=False, unique=True)
    post_id = Column(BigInteger, ForeignKey("user_posts.id"))
    reg_date = Column(DateTime)

    post_fk = relationship(UserPost, lazy='subquery')




