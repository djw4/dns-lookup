FROM python:3.13-slim
LABEL maintainer="Daniel W <github@danieljw.net>"

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV APP_SETTINGS="config.ProductionConfig"

CMD ["python", "app.py"]
