# Виджет для Личного кабинета

## Описание:

В проекте разрабатывается виджет для личного кабинета, который показывает несколько последних успешных банковских 
операций клиента

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/ekomendant/PersonalAccount_widget.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

## Модули и примеры использования.

Все операции для проверки работы функций, которые будут описаны ниже, необходимо запускать в модуле main.py.

### Модуль masks.py
Модуль содержит 2 функции:
1. `get_mask_card_number` - функция преобразует номер карты в ее маску.
2. `get_mask_account` - функция преобразует номер счета в маску.

#### Примеры использования

Для проверки функции `get_mask_card_number` запустите код ниже. В переменной `card_number` можно ввести любое 
16-значное число.
```python
from src.masks import get_mask_card_number

card_number = int(7000792289606361)
print(get_mask_card_number(card_number))
```

Для проверки функции `get_mask_account` запустите код ниже. В переменной `account_number` можно ввести любое 
18-значное число.
```python
from src.masks import get_mask_account

account_number = int(73654108430135874305)
print(get_mask_account(account_number))
```

### Модуль widget.py
Модуль содержит 2 функции:
1. `mask_account_card` - функция преобразует данные карты или счета пользователя в маску. Для преобразования 
используются функции из модуля masks.py
2. `get_date` - функция меняет формат даты на ДД.ММ.ГГГГ.

#### Примеры использования

Для проверки функции `mask_account_card` запустите код ниже. В переменной `index` можно ввести любое число от 0 до 7.
В результате на первой строке будут выведены исходные данные, а на второй - преобразованные.
```python
from src.widget import mask_account_card

examples = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]
index = int(1)
print(examples[index])
print(mask_account_card(examples[index]))
```

Для проверки функции `get_date` запустите код ниже. В переменной `date` можно ввести любую дату в формате 
«YYYY-MM-DDTHH:MM.ssssss».
```python
from src.widget import get_date

date = str("2024-03-11T02:26:18.671407")
print(get_date(date))
```

### Модуль processing.py
Модуль содержит 2 функции:
1. `filter_by_state` - функция фильтрует операции клиента по заданному статусу.
2. `sort_by_date` - функция сортирует операции клиента по дате.

Для проверки функций запустите код ниже. В переменной `state` можно ввести `"EXECUTED"` или `"CANCELED"`,
а в переменной `reverse` указать `True` или `False`
```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
state = "CANCELED"
reverse = True

print("Функция filter_by_state")
for element in filter_by_state(operations, state):
    print(element)

print("\nФункция sort_by_date")
for element in sort_by_date(operations, reverse):
    print(element)
```

### Модуль generators.py
Модуль содержит 3 функции:
1. `filter_by_currency` - функция поочередно выдает транзакции, соответствующие заданной валюте.
2. `transaction_descriptions` - функция возвращает описание каждой транзакции по очереди.
3. `card_number_generator` - функция поочередно генерирует номера банковских карт в заданном диапазоне.

#### Примеры использования

Для проверки функции `filter_by_currency` запустите код ниже. В переменной `currency` можно ввести `"RUB"` или `"USD"`.
```python
import json

from src.generators import filter_by_currency

with open("data/operations.json", "r", encoding="utf-8") as json_file:
    transactions = json.load(json_file)

currency = "RUB"

currency_transactions = filter_by_currency(transactions, currency)
for _ in range(2):
    print(next(currency_transactions))
```

Для проверки функции `transaction_descriptions` запустите код ниже. 
```python
import json

from src.generators import transaction_descriptions

with open("data/operations.json", "r", encoding="utf-8") as json_file:
    transactions = json.load(json_file)

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
```

Для проверки функции `card_number_generator` запустите код ниже. В переменных `start_number` и `finish_number` можно 
ввести любые числа в диапазоне от 1 до 9999999999999999.
```python
from src.generators import card_number_generator

start_number = 1
finish_number = 5

for card_number in card_number_generator(start_number, finish_number):
    print(card_number)
```

### Модуль decorators.py
Модуль содержит функцию-декоратор `log`, которая логирует результаты выполнения декорируемой функции или возникшие 
ошибки. Декоратор может принимать файл для записи логов.

#### Примеры использования

Для проверки функции `log` запустите код ниже. При вызове декоратора в качестве аргумента можно передать переменную 
`filename_exist` (для записи логов в файл) или `filename_not_exist` (для вывода результатов в консоль). Для получения 
лога с ошибкой при вызове функции `my_function` необходимо указать некорректный перечень аргументов
```python
import os

from src.decorators import log

filename_exist = os.path.join(os.path.dirname(__file__), "mylog.txt")
filename_not_exist = ""


@log(filename_exist)
def my_function(x: int, y: int) -> int:
    """Функция складывает 2 числа"""
    return x + y


my_function(1, 2)
```

### Модуль utils.py
Модуль содержит 2 функции:
1. `convert_json_transactions` - функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о 
финансовых транзакциях.
2. `get_amount` - функция принимает транзакцию в виде словаря и возвращает сумму операции (если валюта отличается от 
RUB, то вызывает функцию convert_currency для конвертации).

Для проверки функций запустите код ниже. В переменной `number` моно указать любое число от 0 до 99.
```python
import os

from src.utils import convert_json_transactions, get_amount

filename = os.path.join(os.path.dirname(__file__), "data", "operations.json")
transactions = convert_json_transactions(filename)
number = 5

#Проверка функции convert_json_transactions
print(transactions)

#Проверка функции get_amount
print(get_amount(transactions[number]))
```

### Модуль external_api.py
Модуль содержит функции `convert_currency` которая обращается к API ресурса https://apilayer.com/ и конвертирует сумму 
из исходной валюты на рубли (по курсу на переданную дату).- функция фильтрует операции клиента по заданному статусу.

Для работы функции необходимо получить API-ключ к ресурсу. Затем:
1. в основной директории проекта создать копию файла `.env.example`,
2. переименовать файл в `.env`,
3. указать полученный API-ключ в переменной `API_KEY`.

Для проверки функций запустите код ниже. В переменных `from_currency`, `amount` и `date` можно ввести иные значения (с 
сохранением формата данных).
```python
from src.external_api import convert_currency

from_currency = "USD"
amount = "8221.37"
date = "2019-07-03"
print(convert_currency(from_currency, amount, date))
```

## Тестирование:

Тесты всех функций реализованы в директории `tests`. 
Для запуска тестов введите в терминале команду:
```
pytest
```

Для формирования отчета о покрытии тестами введите в терминале команду:
```
pytest --cov=src --cov-report=html
```
Результат покрытия тестами в HTML-формате можно посмотреть в [отчете](htmlcov\index.html).  

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).
