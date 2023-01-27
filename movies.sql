CREATE DATABASE movies;
use movies;

CREATE TABLE movies (
  movie_id INT NOT NULL,
  title VARCHAR(200),
  imdbId VARCHAR(10),
  tmdbId VARCHAR(10),
  date BIGINT NOT NULL,
  PRIMARY KEY (movie_id)
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
  PRIMARY KEY (user_id, movie_id, tag, time_stamp),
  FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

LOAD DATA INFILE '/var/lib/mysql-files/new_movies.csv' 
INTO TABLE movies 
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/ratings.csv' 
INTO TABLE ratings
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/new_genres.csv' 
INTO TABLE genres
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/tags.csv' 
INTO TABLE tags
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;





-- CREATE TABLE shop (
--     article INT UNSIGNED  DEFAULT '0000' NOT NULL,
--     dealer  CHAR(20)      DEFAULT ''     NOT NULL,
--     price   DECIMAL(16,2) DEFAULT '0.00' NOT NULL,
--     PRIMARY KEY(article, dealer));
-- INSERT INTO shop VALUES
--     (1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),
--     (3,'C',1.69),(3,'D',1.25),(4,'D',19.95);