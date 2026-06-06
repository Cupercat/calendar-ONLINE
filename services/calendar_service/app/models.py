from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class CalendarEvent(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    user_id = Column(Integer)  # ссылка на Auth сервис