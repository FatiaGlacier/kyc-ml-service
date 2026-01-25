FROM python:3.12.2

COPY requirements_app.txt /requirements_app.txt
RUN pip install -r /requirements_app.txt

WORKDIR /app

COPY ./app/main.py /app
COPY ./app/app_config.py /app
COPY ./app/api /app/api
COPY ./app/services /app/services
COPY ./app/utils /app/utils

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

RUN touch /app/__init__.py && \
    touch /app/api/__init__.py && \
    touch /app/services/__init__.py && \
    touch /app/utils/__init__.py

RUN mkdir -p /app/temp/frames /app/temp/videos

EXPOSE 8000

# Default command
CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]