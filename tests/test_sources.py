from unittest.mock import patch

import pandas as pd

from src.sources import import_csv_transactions, import_excel_transactions


# Проверка успешного открытия и чтения файла CSV
@patch("pandas.read_csv")
@patch(
    "pandas.DataFrame.to_dict",
    return_value=[{"id": 441945886, "state": "EXECUTED"}, {"id": 41428829, "state": "EXECUTED"}],
)
def test_import_csv_transactions_success(mock_to_dict, mock_read_csv):
    mock_df = pd.DataFrame({"id": [441945886, 41428829], "state": ["EXECUTED", "EXECUTED"]})
    mock_read_csv.return_value = mock_df

    assert import_csv_transactions("test_file.csv") == [
        {"id": 441945886, "state": "EXECUTED"},
        {"id": 41428829, "state": "EXECUTED"},
    ]

    mock_read_csv.assert_called_once_with("test_file.csv", delimiter=";")
    mock_to_dict.assert_called_once_with(orient="records")


# Проверка функции, если файл CSV не найден
@patch("pandas.read_csv", side_effect=FileNotFoundError)
def test_import_csv_transactions_no_file(mock_read_csv):
    assert import_csv_transactions("test_file.csv") == []


# Проверка успешного открытия и чтения файла EXCEL
@patch("pandas.read_excel")
@patch(
    "pandas.DataFrame.to_dict",
    return_value=[{"id": 441945886, "state": "EXECUTED"}, {"id": 41428829, "state": "EXECUTED"}],
)
def test_import_excel_transactions_success(mock_to_dict, mock_read_excel):
    mock_df = pd.DataFrame({"id": [441945886, 41428829], "state": ["EXECUTED", "EXECUTED"]})
    mock_read_excel.return_value = mock_df

    assert import_excel_transactions("test_file.xlsx") == [
        {"id": 441945886, "state": "EXECUTED"},
        {"id": 41428829, "state": "EXECUTED"},
    ]

    mock_read_excel.assert_called_once_with("test_file.xlsx")
    mock_to_dict.assert_called_once_with(orient="records")


# Проверка функции, если файл EXCEL не найден
@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_import_excel_transactions_no_file(mock_read_excel):
    assert import_excel_transactions("test_file.xlsx") == []
