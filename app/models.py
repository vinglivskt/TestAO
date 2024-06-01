from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base


class Request(Base):

    """  Модель для таблицы t_request  """

    __tablename__ = "t_request"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("t_client.id"))
    area_id = Column(Integer, ForeignKey("t_area.id"))

    client = relationship("Client", back_populates="requests")
    area = relationship("Area", back_populates="requests")


class Client(Base):

    """ Модель для таблицы t_client """

    __tablename__ = "t_client"

    id = Column(Integer, primary_key=True, index=True)
    fullname_client = Column(String, index=True)

    requests = relationship("Request", back_populates="client")


class Area(Base):

    """ Модель для таблицы t_area """

    __tablename__ = "t_area"

    id = Column(Integer, primary_key=True, index=True)
    fullname_area = Column(String, index=True)

    requests = relationship("Request", back_populates="area")
