from sqlalchemy import Column, Integer, String, Float, Date
from app.core.db import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)  # Specify max length
    genre = Column(String(255), nullable=False)  # Specify max length
    language = Column(String(255), nullable=False)  # Specify max length
    release_date = Column(Date, nullable=False)
    duration = Column(Float, nullable=False)
    description = Column(String(1000), nullable=True)  # Optionally increase for longer text



class MoviePoster(Base):
    __tablename__ = "movie_posters"

    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String(500), nullable=False)
    movie_id = Column(Integer, nullable=False)
