from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import and_


from app.models.theater_model import Theater as TheaterModel
from app.schemas import theater_schema as TheaterSchemas



class TheaterServices:
	@classmethod
	def create_theater(cls, db: Session, theater: TheaterSchemas.TheaterCreate):
		theater_dict = dict(theater)
		db_theater = TheaterModel(**theater_dict)
		db.add(db_theater)
		db.commit()
		db.refresh(db_theater)
		return db_theater