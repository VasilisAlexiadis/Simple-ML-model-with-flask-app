FROM python:3.19-slim

WORKDIR /app_copy
COPY . /app_copy
RUN pip install -r req.txt
CMD python app_copy.py


