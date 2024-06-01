from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
from models import Base
from schemas import SRequest
from crud import filter_requests

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Создание экземпляра FastAPI
app = FastAPI()


def get_db():
    """ Зависимость для получения сессии базы данных """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/requests/", response_model=List[SRequest])
def read_requests(
        fullname_area: str = None,
        fullname_client: str = None,
        db: Session = Depends(get_db)):
    """ Определение маршрута для получения запросов с фильтрацией """

    requests = filter_requests(db, fullname_area, fullname_client)
    return requests
