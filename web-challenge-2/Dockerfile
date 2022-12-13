FROM python:3

RUN pip install flask libinjection-python

COPY main.py /
COPY templates/index.html templates/
COPY database.db /

ENV FLASK_APP=main
EXPOSE 8002
CMD flask run --host 0.0.0.0 --port 8002