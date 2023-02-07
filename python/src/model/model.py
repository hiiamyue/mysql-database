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
                
                break
            except:
                print("-")
                time.sleep(1)

        self.db = mydb
        self.cursor = self.db.cursor(dictionary=True)

    def get_default_data(self):
        self.cursor.execute("SELECT * FROM movies")
        movies = self.cursor.fetchall()
        #self.cursor.close()
        return movies

   
    
    def get_genre_type(self):
        self.cursor.execute('SELECT DISTINCT genre FROM genres')
        distinct_genre = self.cursor.fetchall()
        return distinct_genre
    
    def sorting(self,sort_by_date,sort_by_title,sort_by_rating,query):
        if sort_by_date and sort_by_title:
            query= query+'ORDER BY m.release_date,m.title'
        elif sort_by_title:
            query= query+'ORDER BY m.title'
        elif sort_by_date:
            query= query+'ORDER BY m.date'
        return query
    
    def get_film_by_genre_date_rating(self,genre,date_start,date_end,rating_min,rating_max,sort_by_date,sort_by_title,sort_by_rating):
 
        query = "SELECT * FROM movies"

        if genre and date_start and date_end and rating_max and rating_min:
                query = ("""SELECT DISTINCT m.* 
                            \n FROM movies m INNER JOIN genres g
                            \n on m.movie_id = g.movie_id
                            \n AND m.release_date BETWEEN %s AND %s
                            \n AND g.genre IN (%s,%s)
                            \n INNER JOIN ratings r 
                            \n on m.movie_id = r.movie_id
                            \n AND r.rating BETWEEN %s AND %s""")
                query_after_sorting = self.sorting(sort_by_date,sort_by_title,sort_by_rating,query)
        
        self.cursor.execute(query_after_sorting,[date_start,date_end,'Action','Comedy',rating_min,rating_max])

        movies = self.cursor.fetchall()
        return  movies
    
    def close_cursor(self):
        self.cursor.close()