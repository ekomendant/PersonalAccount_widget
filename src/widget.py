from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_details: str) -> str:
    """
    Функция преобразует данные карты или счета пользователя в маску
    :param bank_details: тип и номер карты/счета, тип string
    :return: тип и маска карты/счета, тип string
    """

    if isinstance(bank_details, str):
        if len(bank_details) == 0:
            return "Не указаны данные карты или счета."
        else:
            details_to_list = bank_details.split()
            number = details_to_list[-1]

            if number.isdigit():
                if len(number) == 16:
                    mask = get_mask_card_number(number)
                elif len(number) == 20:
                    mask = get_mask_account(number)
                else:
                    return "Номер карты или счета указан неверно."

                details_to_list[-1] = mask
                return " ".join(details_to_list)
            else:
                return "Номер карты или счета указан неверно."
    else:
        return "Неверные данные карты или счета."


def get_date(date: str) -> str | None:
    """
    Функция меняет формат даты
    :param date: исходная дата, тип string
    :return: измененный формат даты, тип string
    """

    try:
        modified_date = datetime.fromisoformat(date)
        return f"{modified_date:%d.%m.%Y}"
    except ValueError:
        return None
