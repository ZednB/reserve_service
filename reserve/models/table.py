from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from reserve.models import BaseModel
from reserve.core.database import Base


class Table(Base):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    seats = Column(Integer, nullable=False)
    location = Column(String(100), nullable=False)

    reservations = relationship("Reservation", back_populates='tables')
