FROM python:3.9-slim

# Встановлення оновлень і залежностей
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Копіюємо код додатка у контейнер
COPY . /app
WORKDIR /app

# Відкрити порт Flask (за замовчуванням 5000)
EXPOSE 5000

# Команда для запуску сервера
CMD ["python", "app.py"]
