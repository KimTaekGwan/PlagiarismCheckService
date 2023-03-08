from fastapi import APIRouter, HTTPException

from models import User, UserUpdateRequest
from models import db
from uuid import UUID

router = APIRouter()


@router.get("/", tags=['TEST'])
async def root():
    return {"msg": "Hello World"}

@router.get("/users", tags=['TEST'])
async def fetch_users():
    return db

@router.post("/users", tags=['TEST'])
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@router.delete("/users/{user_id}", tags=['TEST'])
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )

@router.put("/users/{user_id}", tags=['TEST'])
async def update_user(user_update: UserUpdateRequest, user_id:UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name:
                user.first_name = user_update.first_name
            if user_update.last_name:
                user.last_name = user_update.last_name
            if user_update.middle_name:
                user.middle_name = user_update.middle_name
            if user_update.roles:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )
