import mysql.connector
import time

class Model:
    def __init__(self) -> None:
        while True:
            try:
                mydb = mysql.connector.connect(
                    host="mysql",
                    user="root",
                    password="sushiroll",
                    database="db"
                )
                print("-")
                break
            except:
                time.sleep(1)

        self.db = mydb
        self.cursor = self.db.cursor(dictionary=True)

    def get_default_data(self):
        self.cursor.execute("SELECT * FROM movies")
        movies = self.cursor.fetchall()
        #self.cursor.close()
        return movies

    def sort_by_date(self):
        self.cursor.execute("SELECT * FROM movies \n ORDER BY release_date")
        movies = self.cursor.fetchall()
        #self.cursor.close()
        return movies
    
    def sort_by_title(self):
        self.cursor.execute("SELECT * FROM movies \n ORDER BY title")
        movies = self.cursor.fetchall()
        #self.cursor.close()
        return movies
    
    def get_genre_type(self):
        self.cursor.execute('SELECT DISTINCT genre FROM genres')
        distinct_genre = self.cursor.fetchall()
        return distinct_genre
    def get_film_by_genre(self,genre):
        query = ("""SELECT * 
                            \n FROM movies WHERE movie_id IN(
                            \n SELECT movie_id From genres
                            \n Where genre = %s)""")
     
        self.cursor.execute(query,genre)
        movies = self.cursor.fetchall()
        return movies
    
    def close_cursor(self):
        self.cursor.close()
    
#     SELECT C.id_car, name, AVG(rating_value) AS average
# FROM car C JOIN rating R 
#       ON C.id_car = R.id_car
# GROUP By C.id_car, name
# ORDER BY average DESC

    def sort_by_rating(self):
        self.cursor.execute("""     SELECT
                                \n  m.*, AVG(r.rating) AS average
                                \n  FROM movies m JOIN ratings r
                                \n  on r.movie_id=m.movie_id 
                                \n  GROUP BY m.movie_id
                                \n  ORDER BY average DESC""")
        movies = self.cursor.fetchall()
        #self.cursor.close()
        return movies
    