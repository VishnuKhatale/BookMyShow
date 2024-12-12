from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from app.core.db import Base
from sqlalchemy.sql import func


# Theater Model
class Theater(Base):
    __tablename__ = "theaters"

    theater_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    address = Column(String(150), nullable=False)
    city_id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)