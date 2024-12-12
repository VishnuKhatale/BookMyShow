from sqlalchemy import Column, Integer,Boolean, String, ForeignKey, TIMESTAMP, Date
from app.core.db import Base
from sqlalchemy.sql import func


# Shows Model
class Shows(Base):
    __tablename__ = "shows"

    show_id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, nullable=False)
    theater_id = Column(Integer, nullable=False)
    screen_id = Column(Integer, default=False)
    show_date = Column(Date, nullable=False)
    show_time = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)