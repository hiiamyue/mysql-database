use db;

CREATE TABLE movies (
  movie_id INT NOT NULL,
  title VARCHAR(200),
  release_date INT NOT NULL,
  imdbId VARCHAR(100),
  tmdbId VARCHAR(10),
  PRIMARY KEY (movie_id),
  FULLTEXT (title)
);

CREATE TABLE ratings (
  user_id INT NOT NULL,
  movie_id INT NOT NULL,
  rating DECIMAL(2,1),
  time_stamp BIGINT NOT NULL,
  PRIMARY KEY (user_id, movie_id)
);
                
CREATE TABLE genres (
  movie_id INT NOT NULL,
  genre VARCHAR(100),
  PRIMARY KEY (movie_id, genre),
  FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

CREATE TABLE tags (
  user_id INT NOT NULL,
  movie_id INT NOT NULL,
  tag VARCHAR(100),
  time_stamp BIGINT NOT NULL,
  PRIMARY KEY (user_id, movie_id,tag),
  FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);



LOAD DATA INFILE '/var/lib/mysql-files/new_movies.csv' 
INTO TABLE movies 
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/ratings.csv' 
INTO TABLE ratings
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/genres.csv' 
INTO TABLE genres
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/tags.csv' 
INTO TABLE tags
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;





