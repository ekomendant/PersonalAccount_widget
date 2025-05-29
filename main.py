from config import PATH
from src.descriptions import search_in_description
from src.processing import filter_by_state, sort_by_date
from src.sources import import_csv_transactions, import_excel_transactions
from src.utils import convert_json_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Функция запрашивает у клиента данные для выборки транзакций и выводит список операций, соответствующих его выбору
    :return: None
    """

    # Приветствие и выбор файла-источника операций
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "\nВыберите необходимый пункт меню:"
        "\n1. Получить информацию о транзакциях из JSON-файла"
        "\n2. Получить информацию о транзакциях из CSV-файла"
        "\n3. Получить информацию о транзакциях из XLSX-файла"
    )

    file_selection = input("\nВведите цифру 1, 2 или 3: ")

    while file_selection not in ["1", "2", "3"]:
        file_selection = input("Номер пункта выбран неверно, введите цифру 1, 2 или 3: ")

    file_format_list = ["JSON", "CSV", "XLSX"]

    if file_selection in ["1", "2", "3"]:
        print(f"Для обработки выбран {file_format_list[int(file_selection)-1]}-файл.")

    # Выбор статуса для фильтрации транзакций
    print(
        "\nВведите статус, по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    state_selection = input("\nВведите статус: ")

    while state_selection.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
        state_selection = input(
            f'Статус операции "{state_selection.upper()}" недоступен. ' f"Введите EXECUTED, CANCELED или PENDING: "
        )

    if state_selection.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Операции отфильтрованы по статусу "{state_selection.upper()}".')

    # Выбор необходимости сортировки по дате
    sorting_by_date = input("\nОтсортировать операции по дате? Да / Нет: ")

    while sorting_by_date.title() not in ["Да", "Нет"]:
        sorting_by_date = input("Неверный выбор, введите Да или Нет: ")

    sorting_by_asc = ""
    if sorting_by_date.title() == "Да":
        sorting_by_asc = input("Для сортировки по возрастанию введите Да, по убыванию - Нет. Да / Нет: ")

        while sorting_by_asc.title() not in ["Да", "Нет"]:
            sorting_by_asc = input("Неверный выбор, введите Да или Нет: ")

        print(
            f"Выбрана сортировка транзакций "
            f"{"по возрастанию даты" if sorting_by_asc.title() == "Да" else "по убыванию даты"}."
        )
    elif sorting_by_date.title() == "Нет":
        print("Сортировка транзакций по дате не требуется.")

    # Выбор необходимости фильтрации по валюте RUB
    filter_rub = input("\nВыводить только рублевые транзакции? Да / Нет: ")

    while filter_rub.title() not in ["Да", "Нет"]:
        filter_rub = input("Неверный выбор, введите Да или Нет: ")

    if filter_rub.title() == "Да":
        print("Выбран вывод только рублевых транзакций.")
    elif filter_rub.title() == "Нет":
        print("Выбран вывод транзакций во всех валютах.")

    # Выбор необходимости фильтрации транзакций по определенному слову
    filter_by_word = input("\nОтфильтровать список транзакций по определенному слову в описании? Да / Нет: ")

    while filter_by_word.title() not in ["Да", "Нет"]:
        filter_by_word = input("Неверный выбор, введите Да или Нет: ")

    word = ""

    if filter_by_word.title() == "Да":
        word = input("Введите слово для фильтрации: ")
        print(f'Выбрана фильтрация по слову "{word.upper()}".')
    elif filter_by_word.title() == "Нет":
        print("Фильтрация по определенному слову не требуется.")

    # Вывод выбранных пользователем параметров
    print(
        f"\nВыбраны следующие параметры для вывода транзакций:"
        f"\n1. Обработка транзакций из {file_format_list[int(file_selection)-1]}-файла."
        f'\n2. Фильтрация операции по статусу "{state_selection.upper()}".'
        f"\n3. Сортировка транзакций "
        f"{"по дате не требуется" if sorting_by_date.title() == "Нет" else
            "по возрастанию даты" if sorting_by_asc.title() == "Да" else "по убыванию даты"}."
        f"\n4. Вывод {"только рублевых транзакций" if filter_rub.title() == "Да" else "транзакций во всех валютах"}."
        f"\n5. Фильтрация по слову {word.upper() if word else "не требуется"}."
    )

    print("\nРаспечатываю итоговый список транзакций...")

    # Получение списка транзакций из файла
    transactions = []
    if file_selection == "1":
        file = str(PATH / "data" / "operations.json")
        transactions = convert_json_transactions(file)
    elif file_selection == "2":
        file = str(PATH / "data" / "transactions.csv")
        transactions = import_csv_transactions(file)
    elif file_selection == "3":
        file = str(PATH / "data" / "transactions_excel.xlsx")
        transactions = import_excel_transactions(file)

    if len(transactions) == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        # Фильтрация списка транзакций по статусу
        state_transactions = filter_by_state(transactions, state=str(state_selection.upper()))
        if len(state_transactions) == 0:
            print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        else:
            # Сортировка по дате
            if sorting_by_date.title() == "Да":
                reverse_value = True if sorting_by_asc.title() == "Нет" else False
                date_sort_list = sort_by_date(state_transactions, reverse_value=reverse_value)
            else:
                date_sort_list = state_transactions

            # Преобразование списка транзакций в единый формат
            unified_list = []
            if file_selection == "1":
                for transaction in date_sort_list:
                    formatted_transaction = {
                        "id": transaction.get("id"),
                        "state": transaction.get("state"),
                        "date": transaction.get("date"),
                        "amount": transaction.get("operationAmount", {}).get("amount"),
                        "currency_name": transaction.get("operationAmount", {}).get("currency", {}).get("name"),
                        "currency_code": transaction.get("operationAmount", {}).get("currency", {}).get("code"),
                        "from": transaction.get("from"),
                        "to": transaction.get("to"),
                        "description": transaction.get("description"),
                    }
                    unified_list.append(formatted_transaction)
            elif file_selection in ["2", "3"]:
                unified_list = date_sort_list

            # Фильтрация по валюте RUB
            if filter_rub.title() == "Да":
                transactions_by_currency = list(filter(lambda x: x["currency_code"] == "RUB", unified_list))
            else:
                transactions_by_currency = unified_list

            if len(transactions_by_currency) == 0:
                print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
            else:
                # Фильтрация по ключевому слову
                if word != "":
                    searched_list = search_in_description(transactions_by_currency, word)
                else:
                    searched_list = transactions_by_currency

                if len(searched_list) == 0:
                    print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
                else:
                    # Вывод итогового списка операций
                    print(f"\nВсего банковских операций в выборке: {len(searched_list)}")
                    for item in searched_list:
                        formatted_date = get_date(str(item.get("date")))
                        from_card = mask_account_card(str(item.get("from")))
                        to_card = mask_account_card(str(item.get("to")))

                        print(
                            f"\n{formatted_date} {item.get("description")}"
                            f"\n{from_card + " -> " if item.get("description") != "Открытие вклада" else ""}{to_card}"
                            f"\nСумма: {item.get("amount")} {item.get("currency_code")}"
                        )
