from pydantic import BaseModel


class SRequestBase(BaseModel):
    """ Схема для RequestBase """

    client_id: int
    area_id: int


class SRequest(SRequestBase):
    """ Схема для Request """

    id: int

    class Config:
        orm_mode = True
