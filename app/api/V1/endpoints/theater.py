from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from app.core.db import engine, get_db
from app.schemas import theater_schema
from app.services.theater_services import TheaterServices
from app.schemas import user_schema
from app.auth.auth import create_access_token, get_current_user 

router = APIRouter()


#theater master
@router.post('/theater/', status_code=status.HTTP_201_CREATED)
def create_theater(theater : theater_schema.TheaterCreate, db: Session = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_user)):
	new_city = TheaterServices.create_theater(db=db, theater=theater)   
	return theater

