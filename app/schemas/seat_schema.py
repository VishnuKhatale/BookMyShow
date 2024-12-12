
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class SeatBase(BaseModel):
    name: str
    screen_id: int
    row_position: int
    column_position : int
    is_deleted: Optional[bool] = False

class SeatCreate(SeatBase):
    pass

class SeatResponse(SeatBase):
    seat_id: int 





