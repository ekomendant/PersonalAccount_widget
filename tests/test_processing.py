from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(operations, operations_executed, operations_canceled):
    assert filter_by_state(operations, "EXECUTED") == operations_executed  # корректные данные
    assert filter_by_state(operations, "CANCELED") == operations_canceled  # корректные данные
    assert filter_by_state(operations, "OPEN") == []  # несуществующий статус
    assert filter_by_state(operations, "") == []  # статус отсутствует
    assert filter_by_state([], "CANCELED") == []  # пустой список
    assert filter_by_state("", "EXECUTED") == []  # некорректный тип данных


def test_sort_by_date(
    operations,
    operations_reverse_true,
    operations_reverse_false,
    operations_same_dates,
    operations_same_dates_reverse_false,
):
    # корректные данные
    assert sort_by_date(operations, True) == operations_reverse_true
    assert sort_by_date(operations, False) == operations_reverse_false

    # пустой список
    assert sort_by_date([], True) == []

    # некорректный тип данных
    assert sort_by_date("", True) == []

    # сортировка одинаковых дат
    assert sort_by_date(operations_same_dates, False) == operations_same_dates_reverse_false
