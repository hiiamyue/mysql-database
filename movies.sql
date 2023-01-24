CREATE DATABASE movies;
use movies;

CREATE TABLE movies (
  movie_id INT,
  title VARCHAR,
  imdbId INT,
  tmdbId INT,
  PRIMARY KEY (movie_id)
);

CREATE TABLE ratings (
  movie_id INT,
  rating DECIMAL(1,1),
  timestamp INT,
  user_id INT,
  PRIMARY KEY (movie_id, user_id)
);

CREATE TABLE genres (
  movie_id INT,
  genre VARCHAR,
  PRIMARY KEY (movie_id),
  FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

CREATE TABLE tags (
  movie_id INT,
  tag VARCHAR,
  timestamp INT,
  user_id INT,
  PRIMARY KEY (movie_id, user_id)
);





-- CREATE TABLE shop (
--     article INT UNSIGNED  DEFAULT '0000' NOT NULL,
--     dealer  CHAR(20)      DEFAULT ''     NOT NULL,
--     price   DECIMAL(16,2) DEFAULT '0.00' NOT NULL,
--     PRIMARY KEY(article, dealer));
-- INSERT INTO shop VALUES
--     (1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),
--     (3,'C',1.69),(3,'D',1.25),(4,'D',19.95);