from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import and_


from app.models.screen_model import Screens as ScreensModel
from app.schemas import screen_schema as ScreensSchemas



class ScreenServices:
	@classmethod
	def create_screen(cls, db: Session, screen: ScreensSchemas.ScreenCreate):
		screen_dict = dict(screen)
		db_screen = ScreensModel(**screen_dict)
		db.add(db_screen)
		db.commit()
		db.refresh(db_screen)
		return db_screen


	@classmethod
	def get_screens(cls, db: Session, limit: int, deleted: bool):
		if deleted:
			db_screens = db.query(ScreensModel).limit(limit).all() 
		else:
			db_screens = (
				db.query(ScreensModel)
				.filter(ScreensModel.is_deleted == False)
				.limit(limit)
				.all()
			)
		return db_screens