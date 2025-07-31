FROM python:3.12-slim-bookworm

LABEL maintainer="The Five Hundred Band"

# Install requirements
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN cd /tmp \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root

WORKDIR /app
COPY ./src /app

EXPOSE 8000

CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
