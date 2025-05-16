import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """
    Декоратор, который логирует результаты выполнения функции или возникшие ошибки
    :param filename: имя файла для записи логов
    :return: на выходе записывает лог в файл (если он указан), либо в консоль
    """

    def wrapper(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any | None:
            start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{start_time} | {function.__name__} ok\n")
                else:
                    print(f"{start_time} | {function.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"{start_time} | {function.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                        )
                else:
                    print(f"{start_time} | {function.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                return None

        return inner

    return wrapper
