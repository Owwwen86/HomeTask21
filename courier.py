from typing import Dict

from abstract_storage import AbstractStorage
from request import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        self.__from: AbstractStorage = storages[self.__request.departure]
        self.__to: AbstractStorage = storages[self.__request.destination]

    def move(self):
        self.__from.remove(product=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.departure}')

        print(f'Курьер везет {self.__request.amount} {self.__request.product}')

        self.__to.add(product=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}')

    def cancel(self):
        self.__from.add(product=self.__request.product, amount=self.__request.amount)
        print(f'Курьер возвращает обратно в {self.__request.departure} {self.__request.amount} {self.__request.product}')
