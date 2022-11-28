class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughSpaceError(BaseError):
    message = 'Недостаточно места'


class UnknownProductError(BaseError):
    message = 'Неизвестный товар'


class NotEnoughProductError(BaseError):
    message = 'Недостаточно товара'


class InvalidRequestError(BaseError):
    message = 'Неправильный запрос'


class UnknownStorage(BaseError):
    message = 'Неизвестный склад'


class TooManyDifferentProductsError(BaseError):
    message = 'Слишком много разных товаров'
