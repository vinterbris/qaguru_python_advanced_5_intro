from fastapi import FastAPI

app = FastAPI()

user_id = 4
user_id_not_found = 23
user_token = 'QpwL5tke4Pnpja7X4'

@app.post('/api/login')
def post_login():
    return {
        "token": user_token
    }


@app.get(f'/api/users/{user_id_not_found}', status_code=404)
def get_user():
    return {}


@app.post('/api/register', status_code=200)
def post_user():
    return {
        "id": user_id,
        "token": user_token
    }


@app.delete(f'/api/users/{user_id}', status_code=204)
def delete_user():
    return ''


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
