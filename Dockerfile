FROM python:3.8-alpine
COPY . /app_copy
WORKDIR /app_copy
RUN pip install -r requirements.txt
