from database import get_db
from database.models import PostPhoto

# получить все или определнную фото


def get_all_or_exact_photo_db(photo_id, user_id):
    db = next(get_db())
    if user_id:
        photo = db.query(PostPhoto).filter_by(user_id=user_id).all()
        return {'status': 1, 'message': photo}
    # если нужна определнная фотография
    elif photo_id:
        exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()
        return {'status': 1, 'message': exact_photo}
    else:
        all_photos = db.query(PostPhoto).all()
        return {'status': 1, 'message': all_photos}

# изменить фото профиля


def change_photo_db(photo_id, new_photo):
    db = next(get_db())
    exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()
    if exact_photo:
        exact_photo.photo_path = new_photo
        db.commit()
        return True
    return False

# удалить фото профиля


def delete_photo_db(photo_id):
    db = next(get_db())
    exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()
    if exact_photo:
        db.delete(exact_photo)
        db.commit()
        return 'фото удалено'
    return 'фото не найдено'