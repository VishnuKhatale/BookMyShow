from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class TheaterBase(BaseModel):
    name: str
    address: str
    city_id: int

class TheaterCreate(TheaterBase):
    pass

class TheaterResponse(TheaterBase):
    theater_id: int




