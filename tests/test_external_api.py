import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import convert_currency

load_dotenv()
API_KEY = os.getenv("API_KEY")


# Проверка успешного выполнения функции с корректным ответом API
@patch("requests.get")
def test_convert_currency_success(mock_get):
    mock_get.return_value.json.return_value = {"result": "992.24"}
    headers = {"apikey": API_KEY}
    mock_get.return_value.status_code = 200
    assert convert_currency("USD", "12.25", "2025-05-16") == (True, "992.24")
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=12.25&date=2025-05-16",
        headers=headers,
    )


# Проверка функции, если API вернул ошибку
@patch("requests.get")
def test_convert_currency_error(mock_get):
    headers = {"apikey": API_KEY}
    mock_get.return_value.status_code = 500
    assert convert_currency("USD", "12.25", "2025-05-16") == (False, "")
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=12.25&date=2025-05-16",
        headers=headers,
    )
