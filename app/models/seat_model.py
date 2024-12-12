from sqlalchemy import Column, Integer,Boolean, String, ForeignKey, TIMESTAMP
from app.core.db import Base
from sqlalchemy.sql import func


# Steats Model
class Seats(Base):
    __tablename__ = "seats"

    seat_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    row_position = Column(Integer, nullable=False)
    column_position = Column(Integer, nullable=False)
    screen_id = Column(Integer, nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)