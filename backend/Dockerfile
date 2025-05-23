FROM python:3.13

WORKDIR /app

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /app/

# Install dependencies via Poetry
RUN poetry install --no-interaction

COPY ./backend/app /app/backend/app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]