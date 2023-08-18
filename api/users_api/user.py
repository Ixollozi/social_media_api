from fastapi import Request
from pydantic import BaseModel
from typing import List, Dict
from database.user_service import register_user_db, check_user_data_db,\
    check_user_password_db, change_user_data, profile_info
from api import app
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def mail_cheker(email):
    if re.fullmatch(regex, email):
        return True
    return False

# модель пользователя


class User(BaseModel):
    name: str
    mail: str
    phone_number: str
    password: str
    user_city: str

# регистрация пользователя


@app.post('/api/registeration')
async def register_user(user_model: User):
    user_data = dict(user_model)
    mail_validation = mail_cheker(user_model.mail)
    if mail_validation:
        try:
            reg_user = register_user_db(**user_data)
            return {'status': 1, 'user_id': reg_user}
        except Exception as e:
            return {'status': 0, 'message': e}
    return {'status': 0, 'message': "invalid email"}

# получить данные пользорвателя по  user_id


@app.get('/api/user')
async def get_user(user_id: int):
    exact_user = profile_info(user_id)
    return {'status': 1, 'user_id': exact_user}

# вход в аккаунт


@app.get('/api/login')
async def login_user(mail: str, password: str):
    # валидация переданной почтой
    mail_validation = mail_cheker(mail)
    if mail_validation:
        login_checker = str(check_user_password_db(mail, password))
        # если все данные верны
        if login_checker.isdigit():
            return {'status': 1, 'user_id': int(login_checker)}
        return {'status': 0, 'message': login_checker}
    return {'status': 0, 'message': 'Invalid email'}

# изменение  данных о пользователе


@app.put('/api/change_profile')
async def change_user_profile(user_id: int, change_nfo: str, new_data: str):
    data = change_user_data(user_id, new_data, change_nfo)
    return {'status': 1, 'message': data}
