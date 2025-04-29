from typing import Optional, List

from pydantic import BaseModel

from reserve.schemas.reservation import Reservation


class TableBase(BaseModel):
    name: str
    seats: str
    location: str


class TableCreate(TableBase):
    pass


class TableUpdate(TableBase):
    name: Optional[str] = None
    seats: Optional[str] = None
    location: Optional[str] = None


class Table(TableBase):
    id: int
    reservations: List[Reservation] = []

    class Config:
        from_attributes = True
