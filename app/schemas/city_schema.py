from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CityBase(BaseModel):
    name: str
    is_deleted: Optional[bool] = False

class CityCreate(CityBase):
    created_at : datetime
    updated_at : datetime

class CityUpdate(CityBase):
    updated_at : datetime


class CityResponse(CityBase):
    city_id: int
 