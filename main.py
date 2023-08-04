from fastapi import FastAPI
from database import Base, engine
# создание таблиц в базе данных
Base = Base.metadata.create_all(bind=engine)

app = FastAPI()
from api.comment_api import coments
from api.hashtag_api import hashtags
from api.posts_api import post
from api.photo_api import photos
from api.users_api import user


