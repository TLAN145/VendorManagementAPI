# Vendor Management API

REST API для управления продавцами на FastAPI.

## Функциональность

- Регистрация нового продавца (POST /vendors)
- Получение списка продавцов с пагинацией и поиском (GET /vendors)
- Получение информации о продавце по ID (GET /vendors/{id})
- Обновление данных продавца (PUT /vendors/{id})
- Удаление продавца (DELETE /vendors/{id})

## Технологии

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic v2
- Uvicorn

## Установка и запуск

```bash
# Клонируем репозиторий
git clone https://github.com/your-username/vendor-management-api.git
cd vendor-management-api

# Создаём виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Устанавливаем зависимости
pip install -r requirements.txt

# Запускаем сервер
uvicorn app.main:app --reload
