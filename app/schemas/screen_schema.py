
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ScreenBase(BaseModel):
    name: str
    # total_seats: int
    total_rows: int
    total_column: int
    theater_id: int
    is_deleted: int

class ScreenCreate(ScreenBase):
    pass

class ScreenResponse(ScreenBase):
    screen_id: int





