FROM python:3.10
RUN pip install --upgrade pip && \
    pip install poetry==1.0 && \
    poetry config virtualenvs.create false

COPY pyproject.toml ./
RUN poetry install

WORKDIR /code
COPY ./app /code/app
CMD ["python","-m","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]