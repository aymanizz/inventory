from abc import ABC, abstractmethod
from typing import List
from sqlalchemy import select
from sqlalchemy.orm.session import Session

from app import db
from app.models import Item


def create_items_repository():
    return SqlalchemyItemsRepository(db.session)


class ItemsRepository(ABC):
    @abstractmethod
    def get(self, id: str):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add(self, item: Item):
        pass

    @abstractmethod
    def update(self, item: Item):
        pass


class SqlalchemyItemsRepository(ItemsRepository):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: str) -> Item:
        return self.session.get(Item, id)

    def get_all(self) -> List[Item]:
        return Item.query.all()

    def add(self, item: Item):
        self.session.add(item)

    def update(self, item: Item):
        # do nothing, sqlalchemy automatically tracks updates
        del item
