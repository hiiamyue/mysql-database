FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=comp0022

COPY ./movies.sql /docker-entrypoint-initdb.d/