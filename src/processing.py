def filter_by_state(states_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей со всеми статусами и отфильтровывает по статусу,
    переданному вторым аргументом
    :param states_list: неотфильтрованный список словарей со всеми статусами
    :param state: отфильтрованный список словарей с выбранным статусом
    :return:
    """

    filtered_states = list()
    for element in states_list:
        if element["state"] == state:
            filtered_states.append(element)

    return filtered_states
