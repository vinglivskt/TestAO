from sqlalchemy.orm import Session
from models import Request, Area, Client


def filter_requests(
        db: Session,
        fullname_area: str = None,
        fullname_client: str = None):
    query = db.query(Request)

    """ Фильтрация запросов по имени области и имени клиента """

    if fullname_area:
        query = query.join(
            Request.area).filter(
            Area.fullname_area == fullname_area)

    if fullname_client:
        query = query.join(
            Request.client).filter(
            Client.fullname_client == fullname_client)

    return query.all()
