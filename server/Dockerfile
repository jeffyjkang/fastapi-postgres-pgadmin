# Pull base image
FROM python:3.11.2-alpine3.17

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry

WORKDIR /server
COPY poetry.lock pyproject.toml /server/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . /server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
