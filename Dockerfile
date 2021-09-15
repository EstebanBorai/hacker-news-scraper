FROM python:3.8

WORKDIR /app

ENV FLASK_APP=src/main.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt .

RUN pip install -r requirements.txt --ignore-installed

COPY src/ .

CMD ["flask", "run"]
