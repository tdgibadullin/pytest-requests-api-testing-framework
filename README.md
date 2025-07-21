# Online Grocery API Test Automation Framework (pytest + Requests)

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![pytest](https://img.shields.io/badge/pytest-grey?logo=pytest)
![Requests](https://img.shields.io/badge/Requests-grey?logo=requests)

[English language](#english) | [Русский язык](#russian)

---
<a id="english"></a>
## Description

This framework automates a checklist for testing the API of the Yandex.Prilavok demo web application.

The project was originally developed as part of completing the Yandex Practicum course "API Test Automation with Python." The project has since been significantly enhanced beyond the course requirements into a full-fledged framework with a broader range of covered scenarios.

The checklist (`checklist.md`) and the implemented automated tests focus on validating the `firstName` field in the body of a `POST` request to the user creation endpoint. The following scenarios are covered:
- valid (2–15 characters) and invalid lengths;
- allowed characters: Russian, English letters, and a hyphen;
- invalid characters: digits, special characters, leading, middle, and trailing spaces;
- `null`, an empty string as the field value, and a missing field in the request body;
- invalid data type: the field value is passed as a number (`int`) instead of a string.

### Key Features

- **Multi-layered architecture.** The framework follows the separation of concerns principle, which **decouples API interaction logic from the test implementation**, ensuring the framework's maintainability. This is reflected in the modules:
  - `client.py`: the API client encapsulating all the HTTP request logic;
  - `helpers.py`: the utility methods that **abstract repeated operations and validations**;
  - `test_first_name.py`: the test cases focused on **high-level actions** rather than low-level HTTP details.

- **Centralized configuration and data management:**
  - all the API client settings (the base URL, paths, and timeout) are stored in a dedicated `configuration.py` module;
  - the request/response data (including the constants for the request headers and body template, as well as for the expected status codes and error messages) is defined in `data.py`, eliminating **magic values** from the codebase.

- **Advanced pytest integration:**
  - the `conftest.py` module provides fixtures for **setting up and injecting dependencies** (namely, API client and helpers instances) into the test methods, ensuring **reusability of dependencies in the tests** and, more broadly, **flexibility and scalability of the framework**;
  - **parameterized testing** via `pytest.mark.parametrize` is used to efficiently test similar scenarios with different input data;
  - known API issues are **documented and tracked in the code** using the expected failures marker (`pytest.mark.xfail`) with explicit reasons.

- **Thorough and precise validations:**
  - positive tests go beyond checking the status code (`201 Created`) by verifying the **integrity of saved data** through comparison with the Users table returned in `.csv` format by the API;
  - negative tests validate not only the error status code (`400 Bad Request`) but also ensure **an exact match** of the error message in the response body with the expected one.

- **Checklist-driven development:**
  - all the automated tests are aligned with the detailed checklist (`checklist.md`), ensuring **full and transparent coverage** of the declared functionality;
  - `id` values in `pytest.mark.parametrize` correspond to the checklist item numbers for easy traceability.

- **Comprehensive documentation:** all the modules, functions, classes, and methods include **informative docstrings** and, where necessary, comments.

---

## Framework Structure

```text
pytest-requests-api-testing-framework/
├── .gitignore         # Files and directories ignored by Git
├── checklist.md       # Checklist automated in the framework
├── client.py          # API client implementation
├── configuration.py   # API client configuration
├── conftest.py        # pytest fixtures
├── data.py            # Request and response data
├── helpers.py         # Helper methods for the tests
├── README.md          # Framework description and usage instructions
├── requirements.txt   # Framework dependencies
└── test_first_name.py # Tests for the firstName field in a request body
```

---

## Tech Stack

- **Language:** Python 3.13
- **Test runner:** pytest
- **Library for HTTP requests:** Requests

---

## Installation and Usage

*Note: The base URL of the tested web application is dynamically generated within the course materials and is of a temporary nature. Therefore, it is currently unavailable. The installation and usage instructions below are provided for reference and to comply with README structure standards.*

### 1. Clone the repository

```bash
git clone https://github.com/tdgibadullin/pytest-requests-api-testing-framework.git
cd pytest-requests-api-testing-framework
```

### 2. Install dependencies

Create a virtual environment:

```bash
python -m venv venv # If the "python" command is not found, try "python3"
```

Activate the virtual environment:

```bash
# For macOS/Linux
source venv/bin/activate

# For Windows (CMD)
venv\Scripts\activate.bat

# For Windows (PowerShell)
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the tests

```bash
pytest
```

---

## Author

[Timur Gibadullin](https://github.com/tdgibadullin) ([tdgibadullin@gmail.com](mailto:tdgibadullin@gmail.com)), 2025

---
<a id="russian"></a>
## Описание

В этом фреймворке автоматизирован чек-лист для тестирования API демонстрационного веб-приложения Яндекс.Прилавок.

Первоначально данный проект был разработан в рамках прохождения курса Яндекс Практикума "Разработка автотестов API на Python". Впоследствии проект был существенно усовершенствован сверх требований курса до полноценного фреймворка, тесты которого покрывают большее число сценариев.

Чек-лист (файл `checklist.md`) и разработанные автотесты охватывают проверки поля `firstName` в теле `POST`-запроса на эндпоинт создания пользователя. Покрываются следующие сценарии:
- длина: корректная (2–15 символов) и недопустимая;
- корректные символы: русские и английские буквы, дефис;
- недопустимые символы: пробел в начале, середине и конце, цифры, спецсимволы;
- `null` в качестве значения поля, пустое значение поля, а также отсутствие поля в теле запроса;
- неверный тип данных: значение поля передано числом (`int`) вместо строки.

### Ключевые особенности

- **Многоуровневая архитектура.** Фреймворк построен по принципу разделения ответственности, что **отделяет логику API-взаимодействий от реализации самих тестов** и обеспечивает его высокую поддерживаемость. Это выражается в модулях:
  - `client.py`: API-клиент, инкапсулирующий всю логику отправки HTTP-запросов;
  - `helpers.py`: вспомогательные методы, которые **абстрагируют повторяющиеся шаги и проверки**;
  - `test_first_name.py`: тест-кейсы, фокусирующиеся на **высокоуровневых действиях**, а не на деталях реализации HTTP-запросов.

- **Централизованное управление конфигурацией и данными:**
  - все настройки API-клиента (базовый URL, пути, таймаут) вынесены в единый модуль `configuration.py`;
  - данные для HTTP-запросов и ответов (включая константы для заголовков и шаблона тела запросов, а также для ожидаемых кодов и сообщений ошибок) хранятся в модуле `data.py`, что **исключает «магические» значения** в коде.

- **Расширенная интеграция с pytest:**
  - модуль `conftest.py` содержит фикстуры для **подготовки и внедрения зависимостей** (а именно, экземпляров API-клиента и хелперов) в тестовые методы, обеспечивая **переиспользование зависимостей в тестах** и, шире, **гибкость и масштабируемость фреймворка**;
  - применяется **параметризация** (`pytest.mark.parametrize`) для эффективного и компактного тестирования аналогичных сценариев с различными входными данными;
  - обнаруженные дефекты API документируются и отслеживаются непосредственно в коде с помощью маркера **ожидаемых падений** (`pytest.mark.xfail`) с указанием точной причины.

- **Комплексные и точные проверки:**
  - позитивные тесты не ограничиваются кодом ответа (`201 Created`), а дополнительно валидируют **целостность данных после их сохранения в системе** путём сверки с таблицей Users, возвращаемой API в формате `.csv`;
  - негативные тесты проверяют не только код ошибки (`400 Bad Request`), но и **полное совпадение текста** в теле ответа с ожидаемым сообщением.

- **Разработка на основе чек-листа:**
  - автотесты фреймворка полностью соответствуют пунктам детального чек-листа (файл `checklist.md`), обеспечивая **полное и прозрачное тестовое покрытие** заявленной функциональности;
  - идентификаторы тестов (`id`) в `pytest.mark.parametrize` совпадают с номерами проверок в чек-листе для удобной навигации.

- **Качественная документация:** все модули, функции, классы и методы содержат **информативные англоязычные докстринги**, а также, при необходимости, комментарии.

---

## Структура фреймворка

```text
pytest-requests-api-testing-framework/
├── .gitignore         # Файлы и директории, игнорируемые Git
├── checklist.md       # Чек-лист, автоматизированный во фреймворке
├── client.py          # Реализация API-клиента
├── configuration.py   # Настройки для API-клиента
├── conftest.py        # Фикстуры pytest
├── data.py            # Данные запросов и ответов
├── helpers.py         # Вспомогательные методы для тестов
├── README.md          # Описание фреймворка и инструкции по запуску
├── requirements.txt   # Зависимости фреймворка
└── test_first_name.py # Тесты для поля firstName в теле запроса
```

---

## Стек технологий
- **Язык**: Python 3.13
- **Тестовый раннер**: pytest
- **Библиотека для HTTP-запросов**: Requests

---

## Установка и запуск

*Примечание: базовый URL тестируемого веб-приложения генерируется динамически в рамках материалов курса и имеет временный характер, ввиду чего на данный момент он недоступен. Инструкция по установке и запуску фреймворка приводится в ознакомительных целях и для соблюдения стандартов структуры README-файла.*

### 1. Клонирование репозитория

```bash
git clone https://github.com/tdgibadullin/pytest-requests-api-testing-framework.git
cd pytest-requests-api-testing-framework
```

### 2. Установка зависимостей

Создайте виртуальное окружение:

```bash 
python -m venv venv # Если команда "python" не найдена, попробуйте "python3"
```

Активируйте виртуальное окружение:

```bash 
# Для macOS/Linux
source venv/bin/activate

# Для Windows (CMD)
venv\Scripts\activate.bat

# Для Windows (PowerShell)
venv\Scripts\Activate.ps1
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

### 3. Запуск тестов

```bash
pytest
```

---

## Автор

[Тимур Гибадуллин](https://github.com/tdgibadullin) ([tdgibadullin@gmail.com](mailto:tdgibadullin@gmail.com)), 2025
