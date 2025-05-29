import re
from collections import Counter
from typing import Any


def search_in_description(transactions_list: list[dict], word: str) -> list[dict]:
    """
    Функция отфильтровывает транзакции, в описании которых содержится строка поиска
    :param transactions_list: список словарей с описанием транзакций
    :param word: строка поиска
    :return: список словарей с транзакциями, содержащими строку поиска
    """

    if not word:
        raise ValueError("Для фильтрации транзакций укажите ключевое слово")
    elif not transactions_list:
        raise ValueError("Не указан список транзакций для фильтрации")
    else:
        final_transactions_list = []
        pattern = re.compile(word, re.IGNORECASE)
        for transaction in transactions_list:
            result = pattern.search(str(transaction.get("description")))
            if result:
                final_transactions_list.append(transaction)
        return final_transactions_list


def count_descriptions(transactions_list: list[dict], categories: list) -> Counter[Any | None]:
    """
    Функция считает количество транзакций по каждой категории (поле "description")
    :param transactions_list: список словарей с описанием транзакций
    :param categories: список категорий (поле "description")
    :return: словарь, где ключи — это названия категорий, а значения — это количество операций в каждой категории
    """

    if not categories:
        raise ValueError("Не указан список категорий для подсчета количества транзакций")
    elif not transactions_list:
        raise ValueError("Не указан список транзакций")
    else:
        counted = Counter(
            transaction.get("description")
            for transaction in transactions_list
            if transaction.get("description") in categories
        )
        return counted
