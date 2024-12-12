from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from app.core.db import engine, get_db
from app.schemas import seat_schema
from app.services.seat_services import SeatServices
from app.schemas import user_schema
from app.auth.auth import create_access_token, get_current_user 
from typing import Annotated

router = APIRouter()


#seat master
@router.post('/seat/', status_code=status.HTTP_201_CREATED)
def create_seat(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], seats : list[seat_schema.SeatCreate], db: Session = Depends(get_db)):

    for seat in seats:
        new_seat = SeatServices.create_seat(db=db, seat=seat)   
    return seats


@router.get("/seat/", response_model=list[seat_schema.SeatResponse], status_code=status.HTTP_200_OK)
def get_seats(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], limit: int = 10, db: Session = Depends(get_db)):
    try:
        db_seats = SeatServices.get_seats(db, limit=limit, deleted=True)
        return db_seats
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching seats: {str(e)}"
        )

