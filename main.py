from courier import Courier
from exeptions import BaseError, TooManyDifferentProductsError
from request import Request

from shop import Shop
from store import Store

shop = Shop(
    items={
        'печенька': 3,
        'ноутбук': 2,
        'елка': 2,
        'кошка': 2,
        'собака': 1,
    }
)

store = Store(
    items={
        'печенька': 10,
        'ноутбук': 20,
        'компьютер': 1,
    }
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        # TODO: Вывести содержимое складов.
        for storage_product in storages:
            print(f'В {storage_product} хранится: {storages[storage_product].get_items()}')

        # TODO: Запросить у пользователя строку.
        user_input = input(
            'Введите строку в формате "Доставить 3 печенька из склад в магазин".\n'
            'Введите "stop" или "стоп", чтобы продолжить:\n',
        )

        if user_input in ('stop', 'стоп'):
            break

        # TODO: Обработать строку, проверить ошибки, определить товар, количество, точки отправления и назначения.
        try:
            request = Request(request_str=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)
        try:
            # TODO: Доставить товар.
            courier.move()
        except TooManyDifferentProductsError as error:
            courier.cancel()
            print(error.message)
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
