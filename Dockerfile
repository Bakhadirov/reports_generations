FROM python:3.9.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /project

RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN POETRY_VIRTUALENVS_CREATE=false poetry install

COPY . .

STOPSIGNAL SIGTERM