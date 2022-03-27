FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV POETRY_VERSION=1.1.13

RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi


COPY ./app /app/app