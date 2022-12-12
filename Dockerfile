FROM python:3.9
RUN pip install --upgrade pip && \
    pip install poetry==1.0

RUN poetry config virtualenvs.create false
COPY pyproject.toml ./
RUN poetry install
RUN poetry lock
RUN poetry update postgres-api
WORKDIR /code
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]