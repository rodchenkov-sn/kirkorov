# syntax=docker/dockerfile:1

FROM python:3.10.7

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY main.py main.py
CMD ["python", "main.py"]
