from api import app
from database.post_service import get_user_hashtag

# поулчить несколько хештегов


@app.get('/api/hashtag')
async def get_hashtags(size: int = 20, page: int = 1):
    pass
# получить фото из определеноого хештега
@app.get('/api/hashtag/<str:hashtag_name>')
async def get_hashtag(hashtag_name: str):
    if hashtag_name:
        exact_hashtag = get_user_hashtag(hashtag_name)
        return {'status': 1, 'message': exact_hashtag}
    return {'status': 0, 'message': 'неверные данные'}
