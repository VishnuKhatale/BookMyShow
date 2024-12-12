from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from app.core.db import engine, get_db
from app.schemas import show_schema
from app.services.show_services import ShowServices
from app.schemas import user_schema
from app.auth.auth import create_access_token, get_current_user 
from typing import Annotated

router = APIRouter()


#show master
@router.post('/show/', status_code=status.HTTP_201_CREATED)
def create_show(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], show : show_schema.ShowCreate, db: Session = Depends(get_db)):
    show = ShowServices.create_show(db=db, show=show)
    return show


@router.get("/show/{movie_id}", status_code=status.HTTP_200_OK)
def get_shows(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], movie_id: int, limit: int = 10, db: Session = Depends(get_db)):
    try:
        db_shows = ShowServices.get_shows(db, limit=limit, movie_id = movie_id)
        return db_shows
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching shows: {str(e)}"
        )

