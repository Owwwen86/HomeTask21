from typing import Dict

from abstract_storage import AbstractStorage
from exeptions import NotEnoughSpaceError, UnknownProductError, NotEnoughProductError


class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, product: str, amount: int) -> None:

        if self.get_free_space() < amount:
            raise NotEnoughSpaceError

        self._items[product] = self._items.get(product, 0) + amount

    def remove(self, product: str, amount: int) -> None:
        if product not in self._items:
            raise UnknownProductError

        if self._items[product] < amount:
            raise NotEnoughProductError

        self._items[product] -= amount
        if self._items[product] == 0:
            self._items.pop(product)

    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self) -> Dict[str, int]:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items)
