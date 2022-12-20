FROM python:3

RUN pip install flask

COPY main.py /
COPY templates/index.html templates/

ENV FLASK_APP=main
EXPOSE 8003
CMD flask run --host 0.0.0.0 --port 8003