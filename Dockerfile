# Dockerfile
FROM python:3.8
WORKDIR /migrations
COPY . /migrations
RUN pip install -r requirements.txt
RUN apt update
RUN apt install -y postgresql-client
EXPOSE 8000
ENTRYPOINT ["./docker-entrypoint.sh"]
