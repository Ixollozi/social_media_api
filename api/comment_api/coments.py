from api import app
from fastapi import Request
from database.post_service import get_comments, public_comment, update_comment, delete_user_comment

# получить коментарии определнного поста


@app.get('/api/comments')
async def get_exact_comments(request: Request):
    #получить json со всеми данными которые пришли из фронта
    data = await request.json()
    # получить ключ пост_ид из дата
    post_id = data.get('post_id')
    if post_id:
        #получить данные из базы
        exact_post_comments = get_comments(post_id)
        return {'status': 1, 'message': exact_post_comments}
    return {'status': 0, 'message': 'Неверный ввод данных'}

#опубликовать коментарий к посту


@app.post('/api/comments')
async def public_comment():
    pass
#изменить коментарий


@app.put('/api/comments')
async def edit_comment():
    pass
#удалить коментарий


@app.delete('/api/comments')
async def delete_comment():
    pass
