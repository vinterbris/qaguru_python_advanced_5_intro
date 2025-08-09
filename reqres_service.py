from fastapi import FastAPI, status, Response

from data.user_data import user_token, users_list, support_data

app = FastAPI()



@app.post('/api/login')
def post_login():
    return {
        "token": user_token
    }


@app.get('/api/users/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: int, response: Response):
    for user in users_list:
        if user['id'] == user_id:
            return {
                'data': user,
                'support': support_data
            }
    response.status_code = status.HTTP_404_NOT_FOUND
    return {}


@app.post('/api/register', status_code=status.HTTP_200_OK)
def post_user():
    return {
        "id": 4,
        "token": user_token
    }


@app.delete('/api/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, response: Response):
    for user in users_list:
        if user['id'] == user_id:
            return ''
    response.status_code = status.HTTP_404_NOT_FOUND
    return ''


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
