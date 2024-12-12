from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from app.core.db import engine, get_db
from app.schemas import city_schema
from app.services.city_services import CityServices

from app.schemas import user_schema
from app.auth.auth import create_access_token, get_current_user 


router = APIRouter()


#city master
@router.post('/city/', status_code=status.HTTP_201_CREATED)
def create_city(city : city_schema.CityCreate, db: Session = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_user)):
	db_city = CityServices.get_city_by_name(db=db, name=city.name)
	if db_city:
		raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="city already registered"
        )
	new_city = CityServices.create_city(db=db, city=city)   
	return new_city


@router.get("/city/", response_model=list[city_schema.CityResponse], status_code=status.HTTP_200_OK)
def get_cities(limit: int = 10, db: Session = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_user)):
    db_city = CityServices.get_cities(db, limit=limit,deleted=True)
    return db_city


@router.get("/city/{city_id}", response_model=city_schema.CityResponse, status_code=status.HTTP_200_OK)
def get_city(city_id:int, db: Session = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_user)):
    db_city = CityServices.get_city_by_id(db, city_id=city_id)
    return db_city

@router.put("/city/{city_id}", response_model=city_schema.CityResponse, status_code=status.HTTP_201_CREATED)
def update_user(city_id:int, city:city_schema.CityUpdate, db: Session = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_user)):
    db_city = CityServices.get_city_by_id(db, city_id)
    if db_city is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="City not found"
        )
    city_up = CityServices.update_city(db, city=city, city_id=city_id )
    return city_up