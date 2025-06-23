FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "django/HW7_getting_started_with_Django/manage.py", "runserver", "0.0.0.0:81"]
