from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ShowBase(BaseModel):
    movie_id: int
    theater_id: int
    screen_id: int
    show_date : date
    show_time: str

class ShowCreate(ShowBase):
    pass

class ShowResponse(ShowBase):
    show_id: int 





