def get_mask_card_number(card_number: int) -> str:
    """
    Функция преобразует номер карты в ее маску
    :param card_number: на вход подается номер карты, type integer
    :return: на выходе получаем маску карты, type string
    """

    card_num_to_str = str(card_number)
    card_mask = f"{card_num_to_str[:4]} {card_num_to_str[4:6]}** **** {card_num_to_str[-4:]}"
    return card_mask


def get_mask_account(account_number: int) -> str:
    """
    Функция преобразует номер счета в маску
    :param account_number: на вход подается номер счета, type integer
    :return: на выходе получаем маску счета, type string
    """

    account_num_to_str = str(account_number)
    account_mask = f"**{account_num_to_str[-4:]}"
    return account_mask
