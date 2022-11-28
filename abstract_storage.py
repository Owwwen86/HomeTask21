from abc import ABC, abstractmethod
from typing import Dict


class AbstractStorage(ABC):

    @abstractmethod
    def add(self, product: str, amount: int) -> None:
        pass

    @abstractmethod
    def remove(self, product: str, amount: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> Dict[str, int]:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass
