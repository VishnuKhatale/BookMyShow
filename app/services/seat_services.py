from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import and_


from app.models.seat_model import Seats as SeatsModel
from app.schemas import seat_schema as SeatSchemas



class SeatServices:
	@classmethod
	def create_seat(cls, db: Session, seat: SeatSchemas.SeatCreate):
		seat_dict = dict(seat)
		db_seat = SeatsModel(**seat_dict)
		db.add(db_seat)
		db.commit()
		db.refresh(db_seat)
		return db_seat


	@classmethod
	def get_seats(cls, db: Session, limit: int, deleted: bool):
		if deleted:
			db_seats = db.query(SeatsModel).limit(limit).all() 
		else:
			db_seats = (
				db.query(SeatsModel)
				.filter(SeatsModel.is_deleted == False)
				.limit(limit)
				.all()
			)
		return db_seats