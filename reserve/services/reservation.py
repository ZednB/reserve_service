from datetime import timedelta, datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from reserve.models.reservation import Reservation
from reserve.schemas.reservation import ReservationCreate


def get_reservations(db: Session):
    """Получение списка брони"""
    return db.query(Reservation).all()


def create_reservations(db: Session, reservation: ReservationCreate):
    start_time = reservation.reservation_time
    end_time = start_time + timedelta(minutes=reservation.duration_minutes)

    # Получаем все брони на этот столик
    existing_reservations = db.query(Reservation).filter(
        Reservation.table_id == reservation.table_id
    ).all()

    for r in existing_reservations:
        r_start = r.reservation_time
        r_end = r_start + timedelta(minutes=r.duration_minutes)

        # Проверяем пересечение интервалов
        if start_time < r_end and r_start < end_time:
            raise HTTPException(
                status_code=409,
                detail='Этот столик занят на установленное время'
            )
        if reservation.reservation_time < datetime.now():
            raise HTTPException(status_code=400, detail="Нельзя забронировать время в прошлом")

    # Если конфликтов нет, создаем бронь
    new_reservation = Reservation(**reservation.dict())
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation


def delete_reservations(db: Session, reservation_id: int) -> bool:
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not reservation:
        return False
    db.delete(reservation)
    db.commit()
    return True
