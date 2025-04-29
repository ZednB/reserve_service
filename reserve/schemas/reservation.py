from datetime import datetime

from pydantic import BaseModel

from reserve.schemas.table import Table


class ReservationBase(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int
    table: Table

    class Config:
        from_attributes = True
