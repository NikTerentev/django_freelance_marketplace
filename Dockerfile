FROM python:3.10

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV POSTGRES_DB=freelance_site
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432

WORKDIR /code

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем проект
COPY . .

EXPOSE 8000

# Запускаем сервер и применяем миграции
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
