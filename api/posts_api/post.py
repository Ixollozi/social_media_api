from api import app

@app.get('/api/post')
async def get_all_post(post_id: int = 0):
    pass

@app.put('/api/post')
async def change_user_post(request):
    response = request.json()
    user_id = response.get('user_id')

@app.delete('/api/post')
async def delete_user_post():
    pass