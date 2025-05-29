import logging

from config import PATH

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH / "logs" / "masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция преобразует номер карты в ее маску
    :param card_number: на вход подается номер карты, type integer
    :return: на выходе получаем маску карты, type string
    """

    logger.info(f"Функция masks.get_mask_card_number запущена c аргументом: {card_number}.")
    if isinstance(card_number, int):
        card_num_to_str = str(card_number)
        if len(card_num_to_str) == 16:
            logger.info("Успешное преобразование номера карты в маску.")
            return f"{card_num_to_str[:4]} {card_num_to_str[4:6]}** **** {card_num_to_str[-4:]}"
        else:
            logger.error("Номер карты указан неверно.")
            return "Номер карты указан неверно. Убедитесь, что ввели 16 цифр."
    elif isinstance(card_number, str):
        new_card_number = card_number.replace(" ", "")
        if new_card_number.isdigit():
            if len(new_card_number) == 16:
                logger.info("Успешное преобразование номера карты в маску.")
                return f"{new_card_number[:4]} {new_card_number[4:6]}** **** {new_card_number[-4:]}"
            else:
                logger.error("Номер карты указан неверно.")
                return "Номер карты указан неверно. Убедитесь, что ввели 16 цифр."
        else:
            logger.error("Номер карты указан неверно.")
            return "Номер карты указан неверно. Убедитесь, что ввели 16 цифр."
    else:
        logger.error("Номер карты указан неверно.")
        return "Номер карты указан неверно. Убедитесь, что ввели 16 цифр."


def get_mask_account(account_number: str) -> str:
    """
    Функция преобразует номер счета в маску
    :param account_number: на вход подается номер счета, type integer
    :return: на выходе получаем маску счета, type string
    """

    logger.info(f"Функция masks.get_mask_account запущена c аргументом: {account_number}.")
    if isinstance(account_number, int):
        account_num_to_str = str(account_number)
        if len(account_num_to_str) == 20:
            logger.info("Успешное преобразование номера счета в маску.")
            return f"**{account_num_to_str[-4:]}"
        else:
            logger.error("Номер счета указан неверно.")
            return "Номер счета указан неверно. Убедитесь, что ввели 20 цифр."
    elif isinstance(account_number, str):
        new_account_number = account_number.replace(" ", "")
        if new_account_number.isdigit():
            if len(new_account_number) == 20:
                logger.info("Успешное преобразование номера счета в маску.")
                return f"**{new_account_number[-4:]}"
            else:
                logger.error("Номер счета указан неверно.")
                return "Номер счета указан неверно. Убедитесь, что ввели 20 цифр."
        else:
            logger.error("Номер счета указан неверно.")
            return "Номер счета указан неверно. Убедитесь, что ввели 20 цифр."
    else:
        logger.error("Номер счета указан неверно.")
        return "Номер счета указан неверно. Убедитесь, что ввели 20 цифр."
