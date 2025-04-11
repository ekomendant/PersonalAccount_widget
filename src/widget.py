from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_details: str) -> str:
    """
    Функция преобразует данные карты или счета пользователя в маску
    :param bank_details: тип и номер карты/счета, тип string
    :return: тип и маска карты/счета, тип string
    """

    details_to_list = bank_details.split()
    number = details_to_list[-1]
    mask = ""

    if len(number) == 16:
        mask = get_mask_card_number(int(number))
    if len(number) == 20:
        mask = get_mask_account(int(number))

    details_to_list[-1] = mask
    return " ".join(details_to_list)


def get_date(date: str) -> str:
    """
    Функция меняет формат даты
    :param date: исходная дата, тип string
    :return: измененный формат даты, тип string
    """

    modified_date = f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    return modified_date
