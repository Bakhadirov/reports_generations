FROM python:3.9.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /project

RUN pip install poetry
COPY pyproject.toml poetry.lock ./
COPY . .
RUN POETRY_VIRTUALENVS_CREATE=false poetry install


CMD ["./manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
STOPSIGNAL SIGTERM