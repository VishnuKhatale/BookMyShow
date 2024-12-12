from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class MovieBase(BaseModel):
    title: str
    genre: str
    language: str
    release_date: date
    duration: float  # Duration in minutes
    description: Optional[str] = None

class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    language: Optional[str] = None
    release_date: Optional[str] = None
    duration: Optional[float] = None
    description: Optional[str] = None

class MoviePosterCreate(BaseModel):
    movie_id: int
    file_path: str  # This will store the JSON-encoded file paths

class MoviePosterCreate(BaseModel):
    file_path: str
    movie_id: int

class MoviePosterResponse(MoviePosterCreate):
    id: int

class MovieResponse(MovieBase):
    id: int
    poster: List[MoviePosterResponse]




