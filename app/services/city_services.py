from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import and_


from app.models.city_model import City as CityModel
from app.schemas import city_schema as CitySchemas




class CityServices:

	@classmethod
	def get_city_by_name(cls, db: Session, name: str):
		return db.query(CityModel).filter(CityModel.name == name).first()


	@classmethod
	def create_city(cls, db: Session, city: CitySchemas.CityCreate):
		city_dict = dict(city)
		db_city = CityModel(**city_dict)
		db.add(db_city)
		db.commit()
		db.refresh(db_city)
		return db_city

	@classmethod
	def get_city_by_id(cls, db: Session, city_id: str):
		return db.query(CityModel).filter(CityModel.city_id == city_id).first()



	@classmethod
	def get_cities(cls, db: Session, limit: int, deleted: bool):
		if deleted:
			db_cities = db.query(CityModel).limit(limit).all() 
		else:
			db_cities = (
				db.query(CityModel)
				.filter(CityModel.is_deleted == False)
				.limit(limit)
				.all()
			)
		return db_cities



	@classmethod
	def update_city(cls, db: Session, city: CitySchemas.CityUpdate, city_id: int):
		db_city = db.query(CityModel).filter(CityModel.city_id == city_id).first()
		for key, value in city:
			if key == "city_id":
				continue
			setattr(db_city, key, value)
		db_city.updated_date = func.now()
		db.commit()
		db.refresh(db_city)
		return db_city