from collections import Counter

import pytest

from src.descriptions import count_descriptions, search_in_description


def test_count_descriptions(transactions):
    # Проверка со списком категорий
    categories = ["Перевод организации", "Перевод с карты на карту", "Открытие вклада"]
    result = Counter({"Перевод организации": 2, "Перевод с карты на карту": 1, "Открытие вклада": 0})
    assert count_descriptions(transactions, categories) == result

    # Проверка на пустой список категорий
    with pytest.raises(ValueError):
        count_descriptions(transactions, [])

    # Проверка на отсутствие списка транзакций
    with pytest.raises(ValueError):
        count_descriptions([], ["Перевод организации"])


def test_search_in_description(transactions):
    # Проверка с ключевым словом
    word = "карт"
    result = [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]
    assert search_in_description(transactions, word) == result

    # Проверка на отсутствие ключевого слова для поиска
    with pytest.raises(ValueError):
        search_in_description(transactions, "")

    # Проверка на отсутствие списка транзакций
    with pytest.raises(ValueError):
        search_in_description([], "перевод")
