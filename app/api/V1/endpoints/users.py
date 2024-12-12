from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from app.core.db import engine, get_db
from app.schemas import user_schema
from app.services.user_services import UserServices
from starlette import status
from sqlalchemy.orm import Session
from app.auth.auth import create_access_token, get_current_user 


router = APIRouter()

@router.post("/token/")
def get_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
   
    db_user = UserServices.get_user_by_email(db, email=form_data.username)
    
    if not db_user or form_data.password != db_user.password:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Generate JWT token
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer", "user" : db_user}



# Register
@router.post("/",response_model=user_schema.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user:user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = UserServices.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=[
                {"field": "email", "error": "Email is already registered"}
            ]
        )

    new_user = UserServices.create_user(db=db, user=user)   
    return new_user
    

@router.get("/", response_model=list[user_schema.UserResponse], status_code=status.HTTP_200_OK)
def get_users(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], limit: int = 10, db: Session = Depends(get_db)):
    db_users = UserServices.get_users(db, limit=limit,deleted=True)
    return db_users



@router.get("/{user_id}", response_model=user_schema.UserResponse, status_code=status.HTTP_200_OK)
def get_user(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], user_id:int, db: Session = Depends(get_db)):
    db_user = UserServices.get_user_by_id(db, user_id=user_id)
    return db_user

@router.put("/{user_id}", response_model=user_schema.UserResponse, status_code=status.HTTP_201_CREATED)
def update_user(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], user_id:int, user:user_schema.UserUpdate, db: Session = Depends(get_db)):
    db_user = UserServices.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    user_up = UserServices.update_user(db, user=user, user_id=user_id )
    return user_up

@router.delete("/{user_id}")
def delete_user(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], user_id:int , db: Session = Depends(get_db)):
    db_user = UserServices.get_user_by_id(db, user_id)
    # if db_user is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
    #     )
    # user_up = UserServices.delete_user(db,user_id=user_id)
    return db_user






