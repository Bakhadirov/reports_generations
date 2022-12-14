##  **Описание проекта:**

*1 часть находится в папке **"script_insert_to_db"**
Конфигурация настроек хранится в **config_upload_csv_to_db.py**
Используется связка pandas+sqlalchemy и загрузка в PostgreSQL.*

*2 часть представляет собой API написанный на DRF проект для управления отображения нужной информации
из базы данных при помощи фреймворка.*

**Реализовано:**
- Регистрация пользователя(становится is_active сразу, в дальнейшем можно регистрацию изменить.)
- Аутентификация пользователя на основе сессии (аутентификация необходима так как есть доступ к финансовым данным)
- Вывод информации из таблиц events и installs1
- Развернута автодокументация 
- Добавлены различные фильтры на edpoint'ы
- Все сенситивные данные вынесены в .env
- docker файл
- Для генерации отчетов временно используется скрипт sql - reports.sql
- Как временное решение для аналитиков, пока API в разработке, следует использовать скрипт left_join.py, где можно задать
    фильтры по дате, названию кампании. Находится в папке script_insert_to_db

**В процессе:**
- тесты (частично написаны для регистрации и входа)
- реализация endpoint'а для генерации отчетов

**Что можно добавить при необходимости:**
- Связку Celery+Redis\RabbitMQ
- Фронт который будет коннектиться к endpoint'ам
- Регистрация  при помощи социальных сетей
- Использование в регистрации токена, JWT


#### Описание установки проекта

1. Если нет poetry, то: pip install poetry
2. poetry init
3. poetry install
4. python manage.py runserver


------------



Описание URL:
1. /api/v1/reports/events/ - вывод данных из таблицы events
2. /api/v1/reports/installs1/ - вывод данных из таблицы installs1
3. api/v1/users/registration/ - регистрация
4. api/v1/users/login/ - логин
5. api/v1/schema/ - yaml schema
6. api/v1/docs/ - схема проекта отображаемая в браузере
7. api/v1/reports/reports_generations/ - вывод сводного отчета(в разработке.Реализовано выборка агрегированных дан-
   ных по одной таблицу, фильты еще не настроены, необходимо некоторое время)
