import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_currency(from_currency: str, amount: str, date: str) -> Any:
    """
    Функция конвертирует сумму в рубли по заданным параметрам
    :param from_currency: исходная валюта
    :param amount: сумма в исходной валюте
    :param date: дата операции (дата курса валюты)
    :return: сумма, конвертированная в рубли по курсу на указанную дату
    """

    to_currency = "RUB"
    url = (
        "https://api.apilayer.com/exchangerates_data/convert"
        + f"?to={to_currency}&from={from_currency}&amount={amount}&date={date}"
    )

    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return True, response.json()["result"]
    else:
        return False, ""
