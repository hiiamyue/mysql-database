# COMP0022 Database
MovieLens dataset:  http://files.grouplens.org/datasets/movielens/ml-latest-small.zip

MYSQL -root password: comp0022

Commands:

docker build -t mysql_db . - build an image
docker run ‘-d’ (for detached mode) mysql_db  - run the container
docker exec -it 'ee4a85ad7bbd' (name of container) /bin/bash - run bash
cd docker-entrypoint-initdb.d 
mysql -pcomp0022
