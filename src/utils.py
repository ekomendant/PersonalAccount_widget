import json
import logging
from datetime import datetime
from json import JSONDecodeError

from config import PATH
from src import external_api

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH / "logs" / "utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def convert_json_transactions(file: str) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param file: путь до JSON-файла
    :return: список словарей с транзакциями, либо пустой список (если нет json-объекта)
    """

    logger.info("Функция utils.convert_json_transactions запущена.")
    try:
        logger.info(f"Открытие файла {file}.")
        with open(file, "r", encoding="utf-8") as json_file:
            try:
                logger.info("Преобразование JSON-данных.")
                transactions = json.load(json_file)
                if isinstance(transactions, list):
                    logger.info("Данные успешно преобразованы.")
                    return transactions
                else:
                    logger.error("Файл не содержит список с JSON-данными, невозможно преобразовать.")
                    return []
            except JSONDecodeError:
                logger.error("Файл не содержал JSON-данных, невозможно преобразовать.")
                return []
    except FileNotFoundError:
        logger.error("Файл не существует, получить данные не удалось.")
        return []


def get_amount(transaction: dict) -> float | str:
    """
    Функция принимает транзакцию в виде словаря и возвращает сумму операции. Если валюта отличается от RUB, то вызывает
    функцию convert_currency для конвертации
    :param transaction: транзакция
    :return: сумма операции
    """

    logger.info("Функция utils.get_amount запущена.")
    try:
        logger.info("Определение параметров транзакции.")
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        trans_date = datetime.fromisoformat(transaction["date"])
        modified_date = f"{trans_date:%Y-%m-%d}"

        if currency == "RUB":
            logger.info("Сумма транзакции успешно получена.")
            return float(amount)
        else:
            logger.info("Обращение к функции external_api.convert_currency для конвертации валюты.")
            status, conversion = external_api.convert_currency(currency, amount, modified_date)
            if status:
                logger.info("Сумма транзакции успешно получена.")
                return float(conversion)
            else:
                logger.error(f"Не удалось конвертировать валюту из {currency} в RUB.")
                return f"Не удалось конвертировать валюту из {currency} в RUB."
    except TypeError:
        logger.error("Транзакция не введена, невозможно определить сумму операции.")
        return "Не введена транзакция."
    except KeyError:
        logger.error("Транзакция введена некорректно, невозможно определить сумму операции.")
        return "Введена некорректная транзакция."
