from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI(title='CRUD FastApi')

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def all_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def add_user(
        username: str = Path(min_length=5, max_length=20, description='Введите имя пользователя', example='Batman'),
        age: int = Path(ge=18, le=100, description='Укажите свой возраст', example='21')) -> str:
    user_id = str(int(max(users,key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: int = Path(ge=1, le=120, description='Укажите ID пользователя, которого хотите изменить', example='2'),
        username: str = Path(min_length=5, max_length=20, description='Введите имя пользователя', example='Superman'),
        age: int = Path(ge=18, le=100, description='Укажите возраст', example='24')) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is registered'

@app.delete('/user/{user_id}')
async def del_user(
        user_id: int = Path(ge=1, le=120,
        description='Укажите ID пользователя, которого нужно удалить', example='4')) -> str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'
