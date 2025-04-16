def filter_by_state(states_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей со всеми статусами и отфильтровывает по статусу,
    переданному вторым аргументом
    :param states_list: неотфильтрованный список словарей со всеми статусами
    :param state: статус для фильтрации, по умолчанию "EXECUTED"
    :return: отфильтрованный список словарей с выбранным статусом
    """

    filtered_states = list()
    for element in states_list:
        if element["state"] == state:
            filtered_states.append(element)

    return filtered_states


def sort_by_date(states_list: list[dict], reverse_value: bool = True) -> list[dict]:
    """
    Функция принимает список словарей со статусами/датами и сортирует его в порядке,
    переданном вторым аргументом
    :param states_list: неотсортированный список словарей
    :param reverse_value: булевое значение для реверса, по умолчанию True
    :return: отсортированный по дате список словарей
    """

    sorted_list = sorted(states_list, key=lambda x: x["date"], reverse=reverse_value)
    return sorted_list
