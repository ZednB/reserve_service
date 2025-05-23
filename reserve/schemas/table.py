from typing import Optional, List

from pydantic import BaseModel
from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from reserve.schemas.reservation import Reservation


class TableBase(BaseModel):
    name: str
    seats: int
    location: str


class TableCreate(TableBase):
    pass


class TableUpdate(TableBase):
    name: Optional[str] = None
    seats: Optional[int] = None
    location: Optional[str] = None


class Table(TableBase):
    id: int

    class Config:
        orm_mode = True
    # reservations: List["Reservation"] = []

    class Config:
        from_attributes = True


def rebuild_table():
    from reserve.schemas.reservation import Reservation
    Table.model_rebuild()


rebuild_table()
