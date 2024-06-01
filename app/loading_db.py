from database import SessionLocal, engine
from models import Base, Client, Area, Request

Base.metadata.create_all(bind=engine)


def loading_into_database():
    """ Функция для загрузки тестовых данных в базу данных """

    db = SessionLocal()
    try:
        # Добавляем тестовые данные для клиентов
        client1 = Client(fullname_client="Alla")
        client2 = Client(fullname_client="Igor")
        client3 = Client(fullname_client="Vlad")

        # Добавляем тестовые данные для областей
        area1 = Area(fullname_area="Russia")
        area2 = Area(fullname_area="USA")

        db.add_all([client1, client2, client3, area1, area2])
        db.commit()

        # Добавляем тестовые данные для запросов
        request1 = Request(client_id=client1.id, area_id=area1.id)
        request2 = Request(client_id=client2.id, area_id=area1.id)
        request3 = Request(client_id=client3.id, area_id=area2.id)

        db.add_all([request1, request2, request3])
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    loading_into_database()
