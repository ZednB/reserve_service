from sqlalchemy.orm import Session

from reserve.models.reservation import Reservation
from reserve.schemas.reservation import ReservationCreate


def get_reservations(db: Session):
    """Получение списка брони"""
    return db.query(Reservation).all()


def create_reservations(db: Session, reservation: ReservationCreate):
    """Создание брони"""
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def delete_reservations(db: Session, reservation_id: int) -> bool:
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not reservation:
        return False
    db.delete(reservation)
    db.commit()
    return True
