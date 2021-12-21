FROM python:3.8.12-bullseye

COPY . /app

WORKDIR /app
RUN pip3 install -r requirements.txt

WORKDIR /app/src

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD ["flask", "run"]