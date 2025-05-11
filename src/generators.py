from typing import Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[dict, None]:
    """
    Функция поочередно выдает транзакции, где валюта операции соответствует заданной
    :param transactions_list: перечень транзакций, тип список словарей
    :param currency: валюта, тип string
    :return: транзакция с соответствующей валютой, тип словарь
    """

    if not currency:
        raise ValueError("Для фильтрации транзакций укажите верную валюту")
    elif not transactions_list:
        raise ValueError("Не указан список транзакция для фильтрации")
    else:
        for transaction in transactions_list:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> Generator[str, None]:
    """
    Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    :param transactions_list: перечень транзакций, тип список словарей
    :return: описание транзакции, тип string
    """

    if not transactions_list:
        raise ValueError("Не указан список транзакций")
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start_number: int, finish_number: int) -> Generator[str, None]:
    """
    Функция поочередно генерирует номера банковских карт в заданном диапазоне
    :param start_number: начало диапазона для генерации, тип число
    :param finish_number: конец диапазона для генерации, тип число
    :return: список карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты
    """

    if not start_number or start_number > 9999999999999999:
        raise ValueError("Числа должны быть в диапазоне от 1 до 9999999999999999")
    elif not finish_number or finish_number > 9999999999999999:
        raise ValueError("Числа должны быть в диапазоне от 1 до 9999999999999999")
    elif finish_number < start_number:
        raise ValueError("Второе число не должно быть меньше первого")
    else:
        for number in range(start_number, finish_number + 1):
            generated_number = f"{"0" * (16 - len(str(number)))}{number}"
            yield f"{generated_number[:4]} {generated_number[4:8]} {generated_number[8:12]} {generated_number[-4:]}"
