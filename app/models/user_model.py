from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, Boolean
from enum import Enum as PyEnum
from sqlalchemy.sql import func
from app.core.db import Base


class UserType(PyEnum):
    customer = "customer"
    admin = "admin"

class User(Base):
    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=True)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(15), nullable=True)
    password = Column(String(255), nullable=False)
    user_type = Column(Enum(UserType), default=UserType.customer, nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)