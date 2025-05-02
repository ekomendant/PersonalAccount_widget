import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(
    transactions, transaction_usd_1, transaction_usd_2, transaction_usd_3, transaction_rub_1, transaction_rub_2
):
    # Проверка на валюту USD
    test_currency_usd = filter_by_currency(transactions, "USD")
    assert next(test_currency_usd) == transaction_usd_1
    assert next(test_currency_usd) == transaction_usd_2
    assert next(test_currency_usd) == transaction_usd_3

    # Проверка на валюту RUB
    test_currency_rub = filter_by_currency(transactions, "RUB")
    assert next(test_currency_rub) == transaction_rub_1
    assert next(test_currency_rub) == transaction_rub_2

    # Проверка на пустое значение валюты
    with pytest.raises(ValueError):
        next(filter_by_currency(transactions, ""))

    # Проверка на отсутствие валюты в списке транзакций
    with pytest.raises(StopIteration):
        next(filter_by_currency(transactions, "EUR"))

    # Проверка на отсутствие списка транзакций
    with pytest.raises(ValueError):
        next(filter_by_currency([], "RUB"))


def test_transaction_descriptions(transactions):
    # Тестирование при корректных входных данных
    test_descriptions = transaction_descriptions(transactions)
    assert next(test_descriptions) == "Перевод организации"
    assert next(test_descriptions) == "Перевод со счета на счет"
    assert next(test_descriptions) == "Перевод со счета на счет"
    assert next(test_descriptions) == "Перевод с карты на карту"
    assert next(test_descriptions) == "Перевод организации"

    # Проверка на отсутствие списка транзакций
    with pytest.raises(ValueError):
        next(transaction_descriptions([]))


def test_card_number_generator():
    # Тестирование при корректных входных данных
    test_generator_1 = card_number_generator(150625, 150627)
    assert next(test_generator_1) == "0000 0000 0015 0625"
    assert next(test_generator_1) == "0000 0000 0015 0626"
    assert next(test_generator_1) == "0000 0000 0015 0627"

    # Стартовое и финишное число равны
    test_generator_2 = card_number_generator(15, 15)
    assert next(test_generator_2) == "0000 0000 0000 0015"

    # Нижняя граница диапазона
    test_generator_3 = card_number_generator(1, 2)
    assert next(test_generator_3) == "0000 0000 0000 0001"
    assert next(test_generator_3) == "0000 0000 0000 0002"

    # Верхняя граница диапазона
    test_generator_4 = card_number_generator(9999999999999998, 9999999999999999)
    assert next(test_generator_4) == "9999 9999 9999 9998"
    assert next(test_generator_4) == "9999 9999 9999 9999"

    # Верхняя граница диапазона
    test_generator_4 = card_number_generator(9999999999999998, 9999999999999999)
    assert next(test_generator_4) == "9999 9999 9999 9998"
    assert next(test_generator_4) == "9999 9999 9999 9999"

    # Атрибуты за границами диапазонов
    with pytest.raises(ValueError):
        next(card_number_generator(0, 2))

    with pytest.raises(ValueError):
        next(card_number_generator(9999999999999999, 10000000000000000))

    # Стартовое число больше финишного
    with pytest.raises(ValueError):
        next(card_number_generator(7, 6))

    # Значения диапазонов не переданы
    with pytest.raises(ValueError):
        next(card_number_generator("", ""))
