#FROM python:3.8-slim-buster
FROM python:3.11.4
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "main.py" ]