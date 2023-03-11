FROM mysql:8.0.32

# ENV MYSQL_ROOT_PASSWORD=sushiroll

COPY ./movies.sql /docker-entrypoint-initdb.d/

COPY ./Normalised/new_movies.csv /var/lib/mysql-files/

COPY ./Normalised/ratings.csv /var/lib/mysql-files/

COPY ./Normalised/genres.csv /var/lib/mysql-files/

COPY ./Normalised/tags.csv /var/lib/mysql-files/

COPY ./Normalised/personality-data.csv /var/lib/mysql-files/

COPY ./Normalised/personality-ratings.csv /var/lib/mysql-files/

