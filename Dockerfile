FROM circleci/python:3.6
MAINTAINER Daniel W &amp;lt;github@danieljw.net&amp;gt;

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt --user

CMD ["python", "app.py"]