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

    
    def get_genre_type(self):
        self.cursor.execute('SELECT DISTINCT genre FROM genres')
        distinct_genre = self.cursor.fetchall()
        return distinct_genre
    

    def sorting(self, sort_by_date, sort_by_title, sort_by_rating,offset, query):
        if sort_by_rating:
            query = query + 'ORDER BY r.rating DESC'
        elif sort_by_title:
            query = query + 'ORDER BY m.title ASC'
        elif sort_by_date:
            query = query + 'ORDER BY m.release_date ASC'
        
        query = query+' LIMIT 23 OFFSET {}'.format(offset)

        return query
    

    def gen_query_for_view(self, genre, date_start, date_end, rating_min, rating_max, page,\
                          select_genre ='\n',select_date ='\n',select_rating ='\n'):
        
        if genre:
            g = tuple(genre)
            select_genre = 'AND g.genre IN {}'.format(g)
        
        if date_start and date_end:
            select_date ='AND m.release_date BETWEEN {0} AND {1}'.format(date_start,date_end)
        elif date_start:
            select_date ='AND m.release_date > {}'.format(date_start)
        elif date_end:
            select_date ='AND m.release_date <{}'.format(date_end)

        if rating_min and rating_max:
            select_rating ='AND r.rating BETWEEN {0} AND {1}'.format(rating_min,rating_max)
        elif rating_min:
            select_rating='AND r.rating > {}'.format(rating_min)
        elif rating_max:
            select_rating ='AND r.rating <{}'.format(rating_max)

        if page:
            offset = (page - 1) * 23

        return select_genre, select_date, select_rating, offset
    
    def get_film_by_genre_date_rating(self,genre,date_start,date_end,rating_min,rating_max,sort_by_date,sort_by_title,sort_by_rating,page):
        selected_genre,selected_date,selected_rating,offset =self.gen_query_for_view(genre,date_start,date_end,rating_min,rating_max,page)
        
        query = ("""SELECT  DISTINCT m.*,CONVERT(r.rating, CHAR) AS rating 
                    \n FROM movies m INNER JOIN genres g
                    \n on m.movie_id = g.movie_id
                    {0}
                    {1}
                    \n INNER JOIN average_rating r 
                    \n on m.movie_id = r.movie_id
                    {2}
                    \n""".format(selected_date, selected_genre, selected_rating))
        
        query_after_sorting = self.sorting(sort_by_date, sort_by_title, sort_by_rating,offset, query)
        self.cursor.execute(query_after_sorting)
        
        movies = self.cursor.fetchall()
        return movies
    
    def search_tmbdID(self,keyword):
        # search by movie title return tmdb id
        query ="""SELECT DISTINCT m.tmdbId FROM movies m
                \n WHERE m.title LIKE '%{}%' """.format(keyword)
        self.cursor.execute(query)
        movies = self.cursor.fetchall()
        return movies
    
    def create_average_table(self):
        query = """CREATE TABLE average_rating(
                SELECT movie_id,AVG(rating) as rating
                FROM ratings
                GROUP BY movie_id
                ORDER BY rating DESC
                    )"""
        self.cursor.execute(query)
    
    def close_cursor(self):
        self.cursor.close()
