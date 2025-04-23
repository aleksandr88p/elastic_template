## Команды для работы с проектом

# elastic_template

---

## 📑 Оглавление / Table of Contents
- [Русский](#русский)
- [English](#english)

---

<a name="русский"></a>
# 🇷🇺 Инструкция (Russian)

## Описание
Этот проект — шаблон для быстрого запуска полнотекстового поиска по юридическим (или любым другим) текстам на базе Elasticsearch. Всё работает через Docker, не требует ручной установки Python или зависимостей на сервере.

## Структура проекта
| Файл / Папка           | Назначение                                                                 |
|------------------------|----------------------------------------------------------------------------|
| docker-compose.yml     | Запуск всех сервисов (elasticsearch, python-скрипты)                        |
| Dockerfile.scripts     | Описание контейнера для python-скриптов                                     |
| requirements.txt       | Python-зависимости для скриптов                                            |
| config.py              | Основные настройки (например, имя индекса)                                 |
| data/                  | Папка с файлами данных (NDJSON)                                            |
| scripts/               | Все python-скрипты для работы с elasticsearch                              |
| README.md              | Эта инструкция                                                             |

## Быстрый старт
1. Собери и запусти сервисы:
    ```bash
    docker-compose up -d
    ```
2. Зайди в контейнер для скриптов:
    ```bash
    docker-compose run --rm scripts
    ```
3. Внутри контейнера запускай нужные скрипты:
    ```bash
    python scripts/create_index.py      # создать индекс
    python scripts/load_data.py         # загрузить данные
    python scripts/searh_test.py        # тестовый поиск
    ```

## Проверка Elasticsearch
```bash
curl http://localhost:9200
```
(или используй IP сервера, если обращаешься снаружи)

## Как адаптировать под другой проект
- Замени `data/` на свои NDJSON-файлы.
- Измени `config.py` (например, имя индекса).
- Адаптируй скрипты в `scripts/` под свою задачу.
- Добавь зависимости в `requirements.txt`.
- Если нужны другие библиотеки — измени `Dockerfile.scripts`.
- Для интеграции с API или UI — добавь новый сервис в `docker-compose.yml`.

## Пример добавления FastAPI
```yaml
  api:
    image: python:3.11-slim
    working_dir: /app
    volumes:
      - ./api:/app
      - ./config.py:/app/config.py
    command: uvicorn main:app --host 0.0.0.0 --port 8000
    depends_on:
      - elasticsearch
    networks:
      - elastic_network
```

## Советы и отладка
- Все действия делай внутри контейнера scripts.
- Если меняешь структуру данных — адаптируй create_index.py и load_data.py.
- Для интеграции с внешним API или UI — просто добавь новый сервис.
- Проверяй логи при ошибках:
    ```bash
    docker-compose logs
    ```

---

<a name="english"></a>
# 🇬🇧 Instruction (English)

## Description
This project is a template for quickly launching full-text search over legal (or any) texts using Elasticsearch. Everything runs via Docker, no manual Python or dependency installation required on the server.

## Project Structure
| File / Folder          | Purpose                                                                   |
|------------------------|---------------------------------------------------------------------------|
| docker-compose.yml     | Launches all services (elasticsearch, python scripts)                     |
| Dockerfile.scripts     | Dockerfile for python scripts container                                   |
| requirements.txt       | Python dependencies for scripts                                           |
| config.py              | Main config (e.g. index name)                                            |
| data/                  | Folder with data files (NDJSON)                                           |
| scripts/               | All python scripts for working with elasticsearch                         |
| README.md              | This instruction                                                          |

## Quick Start
1. Build and run services:
    ```bash
    docker-compose up -d
    ```
2. Enter the scripts container:
    ```bash
    docker-compose run --rm scripts
    ```
3. Inside the container, run needed scripts:
    ```bash
    python scripts/create_index.py      # create index
    python scripts/load_data.py         # load data
    python scripts/searh_test.py        # test search
    ```

## Check Elasticsearch
```bash
curl http://localhost:9200
```
(or use server IP if accessing externally)

## How to adapt for another project
- Replace `data/` with your own NDJSON files.
- Edit `config.py` (e.g., index name).
- Adapt scripts in `scripts/` for your needs.
- Add dependencies to `requirements.txt`.
- If you need other libraries, change `Dockerfile.scripts`.
- For API or UI integration, add a new service in `docker-compose.yml`.

## Example: adding FastAPI
```yaml
  api:
    image: python:3.11-slim
    working_dir: /app
    volumes:
      - ./api:/app
      - ./config.py:/app/config.py
    command: uvicorn main:app --host 0.0.0.0 --port 8000
    depends_on:
      - elasticsearch
    networks:
      - elastic_network
```

## Tips & Debugging
- Do everything inside the scripts container.
- If you change data structure, adapt create_index.py and load_data.py.
- For integration with external API or UI, just add a new service.
- Check logs if errors occur:
    ```bash
    docker-compose logs
    ```

---

## Переключение языка / Language Switch
- [К русской инструкции](#русский)
- [To English instruction](#english)
  ```bash
  docker volume inspect elastic_template_elasticsearch_data
  ```
- Удаление volume (осторожно!):
  ```bash
  docker volume rm elastic_template_elasticsearch_data
  ```