from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP,Boolean
from app.core.db import Base
from sqlalchemy.sql import func


# City Model
class City(Base):
    __tablename__ = "cities"

    city_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, unique=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)