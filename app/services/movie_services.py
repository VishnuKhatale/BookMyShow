from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import and_


from app.models.movie_model import Movie as MovieModel, MoviePoster
from app.schemas import movie_schema as MovieSchemas



class MovieServices:
	@classmethod
	def create_movie(cls, db: Session, movie: MovieSchemas.MovieCreate):
		movie_dict = dict(movie)
		db_movie = MovieModel(**movie_dict)
		db.add(db_movie)
		db.commit()
		db.refresh(db_movie)
		return db_movie

	# @classmethod
	def create_movie_poster(db: Session, poster: MovieSchemas.MoviePosterCreate):
		poster_dict = dict(poster)
		db_poster = MoviePoster(**poster_dict)
		db.add(db_poster)
		db.commit()
		db.refresh(db_poster)
		return db_poster 

	@classmethod
	def get_movie_by_id(cls, db: Session, movie_id: str):
		return db.query(MovieModel).filter(MovieModel.id == movie_id).first()

	@classmethod
	def get_movies(cls, db: Session, limit: int, deleted: bool):
		if deleted:
			db_movies = db.query(MovieModel).limit(limit).all() 
		else:
			db_movies = (
				db.query(MovieModel)
				.filter(MovieModel.is_deleted == False)
				.limit(limit)
				.all()
			)

		return db_movies


	@classmethod
	def get_posters(cls, db: Session, movie_id: int):
		# Your logic to fetch posters using movie_id
		posters = db.query(MoviePoster).filter(MoviePoster.movie_id == movie_id).all()
		return posters


	@classmethod	
	def update_movie(db: Session, movie_id: int, movie: MovieSchemas.MovieUpdate):
	    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
	    
	    if not db_movie:
	        return None
	    
	    for key, value in movie.dict(exclude_unset=True).items():
	        setattr(db_movie, key, value)
	    
	    db.commit()
	    db.refresh(db_movie)
	    return db_movie
	    
	@classmethod
	def update_movie_poster(db: Session, poster: MovieSchemas.MoviePosterCreate):
	    db_movie_poster = db.query(models.MoviePoster).filter(models.MoviePoster.movie_id == poster.movie_id).first()

	    if db_movie_poster:
	        db_movie_poster.file_path = json.dumps(poster.file_path)
	    else:
	        new_poster = models.MoviePoster(movie_id=poster.movie_id, file_path=json.dumps(poster.file_path))
	        db.add(new_poster)

	    db.commit()
	    db.refresh(db_movie_poster)
	    return db_movie_poster