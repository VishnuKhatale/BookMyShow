from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from app.core.db import get_db
from app.schemas import movie_schema
from app.services.movie_services import MovieServices
from app.schemas import user_schema
from app.auth.auth import create_access_token, get_current_user 
import json
from typing import Annotated

router = APIRouter()

@router.post('/movie/', status_code=201)
async def create_movie(
    current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)],
    title: str = Form(...),
    genre: str = Form(...),
    language: str = Form(...),
    release_date: str = Form(...), 
    duration: float = Form(...),
    description: str = Form(...),
    files: list[UploadFile] = File(...),
    db: Session = Depends(get_db)
):
    movie_data = {
        "title": title,
        "genre": genre,
        "language": language,
        "release_date": release_date,
        "duration": duration,
        "description": description
    }

    try:
        movie = movie_schema.MovieCreate(**movie_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    db_movie = MovieServices.create_movie(db=db, movie=movie)

    uploaded_file_paths = []
    for file in files:
        valid_file_types = ["image/jpeg", "image/png"]
        if file.content_type not in valid_file_types:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid file type: {file.content_type}. Only JPEG and PNG are allowed."
            )
        file_path = f"static/uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        uploaded_file_paths.append(file_path)

    poster_data = {
        "file_path": json.dumps(uploaded_file_paths),
        "movie_id": db_movie.id
    }

    posters = movie_schema.MoviePosterCreate(**poster_data)
    poster_db = MovieServices.create_movie_poster(db=db, poster=posters)

    return {
        "movie": movie.dict(),
        "poster": posters.dict() 
    }


@router.get("/movie/", response_model=list[movie_schema.MovieResponse], status_code=status.HTTP_200_OK)
def get_movies(current_user: Annotated[user_schema.UserResponse, Depends(get_current_user)], limit: int = 10, db: Session = Depends(get_db)):
    try:
        db_movies = MovieServices.get_movies(db, limit=limit, deleted=True)
        for movie in db_movies:
            movie.poster = MovieServices.get_posters(db, movie.id)
        
        return db_movies
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching movies: {str(e)}"
        )
  

@router.get("/movie/{movie_id}", status_code=status.HTTP_200_OK)
def get_movie(movie_id:int, db: Session = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_user)):
    db_movie = MovieServices.get_movie_by_id(db, movie_id=movie_id)
    db_movie.poster = MovieServices.get_posters(db, movie_id)
    return db_movie

