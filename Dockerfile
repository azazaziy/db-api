FROM python:3.9
RUN pip install --upgrade pip && \
    pip install poetry==1.0

COPY pyproject.toml ./
RUN poetry install --no-dev
WORKDIR /code
COPY ./app /code/app
CMD ["python","-m","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]