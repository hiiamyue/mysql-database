FROM mysql:8.0.32

ENV MYSQL_ROOT_PASSWORD=comp0022

COPY ./movies.sql /docker-entrypoint-initdb.d/

COPY ./Normalised/movies.csv /var/lib/mysql-files/

COPY ./Normalised/ratings.csv /var/lib/mysql-files/

COPY ./Normalised/new_genres.csv /var/lib/mysql-files/

COPY ./Normalised/tags.csv /var/lib/mysql-files/