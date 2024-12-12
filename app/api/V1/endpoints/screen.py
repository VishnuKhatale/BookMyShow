from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from app.core.db import engine, get_db
from app.schemas import screen_schema
from app.services.screen_services import ScreenServices
from app.schemas import user_schema
from app.auth.auth import create_access_token, get_current_user 
from typing import Annotated


router = APIRouter()


#screen master
@router.post('/screen/', status_code=status.HTTP_201_CREATED)
def create_screen(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], screen : screen_schema.ScreenCreate, db: Session = Depends(get_db)):
	new_screen = ScreenServices.create_screen(db=db, screen=screen)   
	return screen


@router.get("/screen/", response_model=list[screen_schema.ScreenResponse], status_code=status.HTTP_200_OK)
def get_screens(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], limit: int = 10, db: Session = Depends(get_db)):
    try:
        db_screen = ScreenServices.get_screens(db, limit=limit, deleted=True)

        return db_screen
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while fetching screen: {str(e)}"
        )






