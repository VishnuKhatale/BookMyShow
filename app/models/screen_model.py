from sqlalchemy import Column, Integer,Boolean, String, ForeignKey, TIMESTAMP
from app.core.db import Base
from sqlalchemy.sql import func


# Screen Model
class Screens(Base):
    __tablename__ = "screens"

    screen_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    total_seats = Column(Integer, nullable=True)
    total_rows = Column(Integer, nullable=False)
    total_column = Column(Integer, nullable=False)
    theater_id = Column(Integer, nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)