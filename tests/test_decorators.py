import os

from src.decorators import log


def test_log_in_file():
    filename = os.path.join(os.path.dirname(__file__), "testlog.txt")

    @log(filename)
    def my_test_function_in_file(x, y):
        return x + y

    # Проверка корректной работы функции с записью лога в файл
    my_test_function_in_file(2, 3)
    with open(filename, "r", encoding="utf-8") as file:
        func_log = file.read().split("\n")
    assert func_log[-2][22:] == "my_test_function_in_file ok"

    # Проверка ошибки работы функции с записью лога в файл
    my_test_function_in_file(2, 3, 7)
    with open(filename, "r", encoding="utf-8") as file:
        func_log = file.read().split("\n")
    assert func_log[-2][22:] == "my_test_function_in_file error: TypeError. Inputs: (2, 3, 7), {}"


def test_log_in_terminal(capsys):
    filename = ""

    @log(filename)
    def my_test_function_in_terminal(x, y):
        return x + y

    # Проверка корректной работы функции с выводом в консоль
    assert my_test_function_in_terminal(2, 3) == 5
    captured = capsys.readouterr()
    assert captured.out[22:] == "my_test_function_in_terminal ok\n"

    # Проверка ошибки работы функции с выводом в консоль
    assert my_test_function_in_terminal(2, 3, 7) is None
    captured = capsys.readouterr()
    assert captured.out[22:] == "my_test_function_in_terminal error: TypeError. Inputs: (2, 3, 7), {}\n"
