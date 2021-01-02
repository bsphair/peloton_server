FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./app/poetry.lock* /app/

RUN poetry install --no-root --no-dev
#ENV POETRY_VERSION=1.0.0
#
#RUN pip install "poetry==$POETRY_VERSION"
#WORKDIR /app
#COPY poetry.lock pyproject.toml /app/
#RUN poetry config virtualenvs.create false \
#  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi


COPY ./app /app/app