FROM alpine:3.14
COPY . /app_copy
WORKDIR /app_copy
RUN pip install -r requirements.txt
CMD python app_copy.py
