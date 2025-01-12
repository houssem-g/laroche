# app/schemas/item.py
from pydantic import BaseModel


class StrictBaseModel(BaseModel):
    class Config:
        extra = "forbid"


class ItemCreate(StrictBaseModel):
    subject: str
    predicate: str
    obj: str


class ItemUpdate(StrictBaseModel):
    old_predicate: str
    new_predicate: str

class QARequest(StrictBaseModel):
    user_query: str

