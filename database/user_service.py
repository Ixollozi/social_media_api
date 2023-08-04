from database.models import User
from datetime import datetime
from database import get_db

# регитсрация пользователя


def register_user_db(name, mail, phone_number, password, user_city):
    db = next(get_db())
    new_user = User(name=name, mail=mail, phone_number=phone_number,
                    password=password, user_city=user_city, reg_date=datetime.now())
    #добавляем в базу
    db.add(new_user)
    # сохраним в базу
    db.commit()
    return new_user.id

# проверка на наличие в базе пользователя


def check_user_data_db(phone_number, mail):
    db = next(get_db())
    #проверка данных на наличие записи в базе
    checker = db.query(User).filter_by(phone_number=phone_number, mail=mail).first()
    #если есть совпадение
    if checker:
        return False
    #если нет совпадения
    return True

# проверка пользователя при входе в аккаунт
def check_user_password_db(mail, password):
    db = next(get_db())
    #проверка данных на наличие записи в базе
    checker = db.query(User).filter_by(mail=mail).first()
    #ессли нашел такйо эмеил, проверяем правильность пароля
    if checker:
        #начинаем сверку пароля
        if checker.password == password:
            return checker.id
        else:
            return 'неверный пароль'
    #если не находит в базе
    return 'неверная почта'

# получить информации о пользователе


def profile_info(user_id):
    db = next(get_db())
    #првоерка пользователя через айди
    exact_user = db.query(User).filter_by(id=user_id).first()
    #если нашел пользователя, передаю всю пользователю
    if exact_user:
        return exact_user.mail, exact_user.phone_number,\
            exact_user.id, exact_user.name, exact_user.reg_date, exact_user.city
    #если не нашел пользователя
    return 'нет такого пользователя'

def change_user_data(user_id, change_info, new_data):
    db = next(get_db())
    #находим пользователя в базе
    exact_user = db.query(User).filter_by(id=user_id).first()
    #проверка того, какую информацию хочет изменить пользователь
    if exact_user:
        if change_info == 'email':
            exact_user.mail = new_data
        elif change_info == 'number':
            exact_user.phone_number = new_data
        elif change_info == 'name':
            exact_user.name = new_data
        elif change_info == 'city':
            exact_user.user_city = new_data
        elif change_info == 'password':
            exact_user.password = new_data
        db.commit()
        return 'данные успешно изменены'
    #а если не находим в базе пользователя
    return 'пользователь не найден'

# сброс пароля


def delete_password(user_id, password):
    db = next(get_db())
    #находим пользователя в базе
    exact_user = db.query(User).filter_by(id=user_id).first()
    #проверка того, какую информацию хочет изменить пользователь
    if exact_user:
        if exact_user.password == password:
            exact_user.password = 'password'
            db.delete(password)
            db.commit()
            return 'пароль успешно сброшен'
        else:
            return 'неверный пароль'
    #а если не находим в базе пользователя
    return 'пользователь не найден'