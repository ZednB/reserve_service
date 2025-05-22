from sqlalchemy.orm import Session

from reserve.models.table import Table
from reserve.schemas.table import TableCreate


def get_tables(db: Session):
    """Получение столика"""
    return db.query(Table).all()


def create_tables(db: Session, table: dict) -> Table:
    """Создание столика"""
    db_table = Table(**table)
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


def delete_tables(db: Session, table_id: int) -> bool:
    """Удаление столика"""
    table = db.query(Table).filter(Table.id == table_id).first()
    if not table:
        return False
    db.delete(table)
    db.commit()
    return True
