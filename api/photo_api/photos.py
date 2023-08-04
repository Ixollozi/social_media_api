from api import app
from fastapi import Request, Body, UploadFile
from database.photo_service import *

# получить все фото


@app.route('/api/photos')
async def get_photos(photo_id: int = 0, user_id: int = 0):
    if photo_id and user_id:
        all_or_exact = get_all_or_exact_photo_db(photo_id, user_id)
        return {'status': 1, 'message': all_or_exact}
    return {'status': 0, 'message': 'Неверный ввод данных'}
# изменить фото профиля


@app.put('/api/photos')
async def change_profile_photo(photo_id: int = Body(...),
                               photo_file: UploadFile = Body(...)):
    if photo_file:
        # сохранить фото в папку
        with open(f'{photo_id}.jpg', 'wb') as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
        change_photo_db(photo_id, f'api/photo_api/photo/{photo_id}.jpg')
    return {'starus': 1, 'message': 'фото успешно изменнено'}

# удалить фото определенного юзера


@app.delete('/api/photos')
async def delete_photo(request: Request):
    data = await request.json()

    photo_id = data['post_id']
    if photo_id:
        delete_photo_db(photo_id)
        return {'status': 1, 'message': 'Фото удалено'}
    return {'status': 0, 'message': 'Неверный ввод данных'}
