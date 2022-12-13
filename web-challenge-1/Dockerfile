FROM python:3

RUN pip install flask

COPY main.py /
COPY templates/loginpage.html templates/
COPY database.db /

ENV FLASK_APP=main
EXPOSE 8001
CMD flask run --host 0.0.0.0 --port 8001