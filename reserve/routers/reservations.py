from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from reserve.core.database import get_db
from reserve.schemas.reservation import Reservation
from reserve.services.reservation import get_reservations

router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.get("/", response_model=List[Reservation])
def list_reservation(db: Session = Depends(get_db)):
    """Полученик списка броней"""
    return get_reservations(db)
