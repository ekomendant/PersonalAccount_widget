import os
from json import JSONDecodeError
from unittest.mock import patch

from dotenv import load_dotenv

from src.utils import convert_json_transactions, get_amount

load_dotenv()
API_KEY = os.getenv("API_KEY")


""" Тестирование функции convert_json_transactions """


# Проверка успешного открытия и чтения JSON-файла
@patch("builtins.open")
@patch("json.load", return_value=[{"id": 441945886, "state": "EXECUTED"}, {"id": 41428829, "state": "EXECUTED"}])
def test_convert_json_transactions_success(mock_load, mock_open):
    file = mock_open.return_value.__enter__.return_value
    assert type(mock_load.return_value) is list
    assert convert_json_transactions("test_file.json") == [
        {"id": 441945886, "state": "EXECUTED"},
        {"id": 41428829, "state": "EXECUTED"},
    ]

    mock_open.assert_called_once_with("test_file.json", "r", encoding="utf-8")
    mock_load.assert_called_once_with(file)


# Проверка функции, если файл не содержит JSON-данные
@patch("builtins.open")
@patch("json.load", return_value="")
def test_convert_json_transactions_incorrect_type(mock_load, mock_open):
    file = mock_open.return_value.__enter__.return_value
    assert type(mock_load.return_value) is not list
    assert convert_json_transactions("test_file.json") == []

    mock_open.assert_called_once_with("test_file.json", "r", encoding="utf-8")
    mock_load.assert_called_once_with(file)


# Проверка функции, если файл пустой
@patch("builtins.open")
@patch("json.load", side_effect=JSONDecodeError("Expecting value", "", 0))
def test_convert_json_transactions_no_data(mock_load, mock_open):
    file = mock_open.return_value.__enter__.return_value
    assert convert_json_transactions("test_file.json") == []

    mock_open.assert_called_once_with("test_file.json", "r", encoding="utf-8")
    mock_load.assert_called_once_with(file)


# Проверка функции, если файл не найден
@patch("builtins.open", side_effect=FileNotFoundError)
def test_convert_json_transactions_no_file(mock_open):
    assert convert_json_transactions("test_file.json") == []


""" Тестирование функции get_amount """


def test_get_amount(operation_rub):
    # Проверка успешного открытия и чтения JSON-файла
    assert get_amount(operation_rub) == 31957.58

    # Проверка функции, если транзакция не содержит нужных данных
    assert get_amount({}) == "Введена некорректная транзакция."

    # Проверка функции, если транзакция не передана
    assert get_amount("") == "Не введена транзакция."


# Проверка функции с запросом к src.external_api.convert_currency (api.status_cose == 200)
@patch("src.external_api.convert_currency")
def test_get_amount_fnc_success(mock_convert_currency, operation_usd):
    mock_convert_currency.return_value = True, "50.12"
    assert get_amount(operation_usd) == 50.12


# Проверка функции с запросом к src.external_api.convert_currency (api.status_cose != 200)
@patch("src.external_api.convert_currency")
def test_get_amount_fnc_error(mock_convert_currency, operation_usd):
    mock_convert_currency.return_value = False, ""
    assert get_amount(operation_usd) == "Не удалось ковертировать валюту из USD в RUB."
