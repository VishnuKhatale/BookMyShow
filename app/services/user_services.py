from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import and_


from app.models.user_model import User as UserModel
from app.schemas import user_schema as UserSchemas

class UserServices:
    @classmethod
    def get_user_by_email(cls, db: Session, email: str):
        return db.query(UserModel).filter(UserModel.email == email).first()

    @classmethod
    def get_user_by_id(cls, db: Session, user_id: str):
        return db.query(UserModel).filter(UserModel.user_id == user_id).first()

    @classmethod
    def get_users(cls, db: Session, limit: int, deleted: bool):
        if deleted:
            db_users = db.query(UserModel).limit(limit).all() 
        else:
            db_users = (
                db.query(UserModel)
                .filter(UserModel.is_deleted == False)
                .limit(limit)
                .all()
            )
        return db_users
    
    @classmethod
    def create_user(cls, db: Session, user: UserSchemas.UserCreate):
        user_dict = dict(user)
        db_user = UserModel(**user_dict)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @classmethod
    def update_user(cls, db: Session, user: UserSchemas.UserUpdate, user_id: int):
        db_user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
        for key, value in user:
            if key == "user_id":
                continue
            setattr(db_user, key, value)
        db_user.updated_date = func.now()
        db.commit()
        db.refresh(db_user)
        return db_user


    @classmethod
    def delete_user(cls, db: Session, user_id: int):
        db_user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
        db_user.is_deleted = True
        db_user.updated_date = func.now()
        db.commit()
        db.refresh(db_user)
        return db_user