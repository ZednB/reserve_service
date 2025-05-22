from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import status

from reserve.core.database import get_db
from reserve.schemas.table import Table, TableCreate

from reserve.services.table import get_tables, create_tables, delete_tables

router = APIRouter(prefix='/tables', tags=['tables'])


@router.get("/", response_model=List[Table])
def list_tables(db: Session = Depends(get_db)):
    """Получение списка столиков"""
    return get_tables(db)


@router.post("/", response_model=Table, status_code=status.HTTP_201_CREATED)
def create_table(table: TableCreate, db: Session = Depends((get_db))):
    """Создание столика"""
    return create_tables(db, table.dict())


@router.delete("/{table_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_table(table_id: int, db: Session = Depends(get_db)):
    """Удаление столика"""
    if not delete_table(table_id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Столик не найден"
        )
    return delete_tables(db, table_id)
