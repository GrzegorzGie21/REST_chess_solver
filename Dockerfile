FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNONBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

COPY . /code/