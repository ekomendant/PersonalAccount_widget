import json
from datetime import datetime
from json import JSONDecodeError

from src import external_api


def convert_json_transactions(file: str) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param file: путь до JSON-файла
    :return: список словарей с транзакциями, либо пустой список (если нет json-объекта)
    """

    try:
        with open(file, "r", encoding="utf-8") as json_file:
            try:
                transactions = json.load(json_file)
                if isinstance(transactions, list):
                    return transactions
                else:
                    return []
            except JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


def get_amount(transaction: dict) -> float | str:
    """
    Функция принимает транзакцию в виде словаря и возвращает сумму операции. Если валюта отличается от RUB, то вызывает
    функцию convert_currency для конвертации
    :param transaction: транзакция
    :return: сумма операции
    """

    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        trans_date = datetime.fromisoformat(transaction["date"])
        modified_date = f"{trans_date:%Y-%m-%d}"

        if currency == "RUB":
            return float(amount)
        else:
            status, conversion = external_api.convert_currency(currency, amount, modified_date)
            if status:
                return float(conversion)
            else:
                return f"Не удалось ковертировать валюту из {currency} в RUB."
    except TypeError:
        return "Не введена транзакция."
    except KeyError:
        return "Введена некорректная транзакция."
