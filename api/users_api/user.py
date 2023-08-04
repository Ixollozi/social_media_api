from fastapi import Request
from pydantic import BaseModel
from typing import List, Dict
from database.user_service import register_user_db, check_user_data_db, check_user_password_db, change_user_data, profile_info
from api import app


# модель пользователя
class User(BaseModel):
    name: str
    mail: str
    phone: str
    password: str
    city: str

# регистрация пользователя
@app.post('/api/registeration')
async def register_user(user_model: User):
    print(user_model)
    return {'status': 1}
