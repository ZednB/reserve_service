from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import status

from reserve.core.database import get_db
from reserve.schemas.reservation import Reservation, ReservationCreate
from reserve.services.reservation import get_reservations, create_reservations, delete_reservations

router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.get("/", response_model=List[Reservation])
def list_reservation(db: Session = Depends(get_db)):
    """Полученик списка броней"""
    return get_reservations(db)


@router.post("/", response_model=Reservation, status_code=status.HTTP_201_CREATED)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    """Создание брони"""
    return create_reservations(db, reservation)


@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    """Удаление брони"""
    if not delete_reservations(db, reservation_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Бронь не найдена')
    return delete_reservations(db, reservation_id)

