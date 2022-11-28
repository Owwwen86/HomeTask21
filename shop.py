from typing import Dict

from base_storage import BaseStorage
from exeptions import TooManyDifferentProductsError


class Shop(BaseStorage):
    def __init__(self, items: Dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, product: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProductsError

        super().add(product, amount)
