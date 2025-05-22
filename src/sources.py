import pandas as pd


def import_csv_transactions(file: str) -> list:
    """
    Функция принимает на вход путь до файла CSV и возвращает список словарей с данными о финансовых транзакциях
    :param file: путь до файла CSV
    :return: список словарей с транзакциями, либо пустой список (если файла не существует)
    """

    try:
        transactions_df = pd.read_csv(file, delimiter=";")
        return transactions_df.to_dict(orient="records")
    except FileNotFoundError:
        return []


def import_excel_transactions(file: str) -> list:
    """
    Функция принимает на вход путь до файла EXCEL и возвращает список словарей с данными о финансовых транзакциях
    :param file: путь до файла EXCEL
    :return: список словарей с транзакциями, либо пустой список (если файла не существует)
    """

    try:
        transactions_df = pd.read_excel(file)
        return transactions_df.to_dict(orient="records")
    except FileNotFoundError:
        return []
