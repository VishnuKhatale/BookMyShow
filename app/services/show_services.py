from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import and_

from fastapi.encoders import jsonable_encoder
from app.models.show_model import Shows as ShowsModel
from app.models.movie_model import Movie as MovieModel
from app.models.theater_model import Theater as TheaterModel
from app.models.screen_model import Screens as ScreensModel

from app.schemas import show_schema as ShowSchemas



class ShowServices:
	@classmethod
	def create_show(cls, db: Session, show: ShowSchemas.ShowCreate):
		show_dict = dict(show)
		db_show = ShowsModel(**show_dict)
		db.add(db_show)
		db.commit()
		db.refresh(db_show)
		return db_show


	@classmethod
	def get_shows(cls, db: Session, limit: int, movie_id=int):
	    db_shows = (
	        db.query(
	            ShowsModel.show_id,
	            ShowsModel.movie_id,
	            ShowsModel.theater_id,
	            ShowsModel.screen_id,
	            ShowsModel.show_date,
	            ShowsModel.show_time,
	            MovieModel.id.label('movie_id'),
	            MovieModel.title,
	            MovieModel.genre,
	            MovieModel.language,
	            MovieModel.release_date,
	            MovieModel.duration,
	            MovieModel.description,
	            ScreensModel.screen_id.label('screen_id'),
	            ScreensModel.name.label('screen_name'),
	            ScreensModel.total_rows,
	            ScreensModel.total_column,
	            ScreensModel.theater_id.label('screen_theater_id'),
	            ScreensModel.is_deleted
	        )
	        .join(MovieModel, ShowsModel.movie_id == MovieModel.id)
	        .join(ScreensModel, ShowsModel.screen_id == ScreensModel.screen_id)
	        .filter(MovieModel.id == movie_id)
	        .limit(limit)
	        .all()
	    )

	    return [show._asdict() for show in db_shows]