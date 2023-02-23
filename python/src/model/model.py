import mysql.connector
import time
import sys
import re

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
        self.__PAGE_SIZE = 28
 

    def get_last_query_found_rows(self):
        query = "SELECT FOUND_ROWS()"
        self.cursor.execute(query)
        movies = self.cursor.fetchall()
        return movies

    def get_movies(self, genres, date_from, date_to, min_rating, max_rating, sort_by, desc,page):



        """_summary_

        Args:
            genres (_type_): _description_
            date_from (_type_): _description_
            date_to (_type_): _description_
            min_rating (_type_): _description_
            max_rating (_type_): _description_
            sort_by (_type_): _description_
            desc (_type_): _description_

        Returns:
            _type_: _description_
        """

        q = self.__gen_movies_query(genres, date_from, date_to, min_rating, max_rating, sort_by, desc, page)

        self.cursor.execute(q)
        movies = self.cursor.fetchall()

        return movies


    def __add_pagination(self, page_num):
        if page_num == None:
            ofset = 0
        else:
            ofset = (int(page_num) - 1) * self.__PAGE_SIZE 

        return "LIMIT {0}, {1};".format(str(ofset), self.__PAGE_SIZE)
        
    
    def __create_date_filter(self, date_from, date_to):
        if date_from is not None and date_to is not None:
            return 'AND release_date BETWEEN {0} AND {1}'.format(date_from,date_to)
        return ""
        
    def __create_rating_filter(self, min_rating, max_rating):
        if min_rating is not None and max_rating is not None:
            return 'AND r.avg_rating BETWEEN {0} AND {1}'.format(min_rating, max_rating)
        return ""
        
    def __create_genre_filter(self, genres):
        if genres is not None:
            return 'AND EXISTS (SELECT * FROM genres, movies WHERE m.movie_id = genres.movie_id and genres.genre in {})'.format(genres)
        return ""
    def __create_sorting_query(self, sort_by, desc):
        
        if sort_by is not None:

            
            if sort_by == "rating":
                sort_by = "r.avg_rating"
            if sort_by == "releasedate":
                sort_by = "release_date"
            if sort_by =="title":
                sort_by = "title"
            
            if desc:
                order = "DESC"
            else:
                order = ""

            return 'ORDER BY {} {}'.format(sort_by, order)
        return ""
  
    def __gen_movies_query(self, genres, date_from, date_to, min_rating, max_rating, sort_by, desc, page):
        #TODO add part for rating

        date_filter = self.__create_date_filter(date_from, date_to)
        genre_filter = self.__create_genre_filter(genres)
        rating_filter = self.__create_rating_filter(min_rating, max_rating)
        sorting = self.__create_sorting_query(sort_by, desc)
        pagination = self.__add_pagination(page)

        query = ("""SELECT DISTINCT SQL_CALC_FOUND_ROWS *
                    \n FROM movies m 
                    \n INNER JOIN ( SELECT GROUP_CONCAT(genre) genres, movie_id
                    \n from genres
                    \n GROUP BY movie_id
                    \n ) g on m.movie_id = g.movie_id
                    \n INNER JOIN ( SELECT CONVERT(AVG(rating), float) AS avg_rating, movie_id
                    \n FROM ratings
                    \n group by movie_id
                    \n ) r on m.movie_id = r.movie_id
                    \n{0}
                    \n{1}
                    \n{2}
                    \n{3}
                    \n{4}
                    \n""".format(date_filter, genre_filter, rating_filter, sorting, pagination))
        
        print(query, file=sys.stderr)
        return query
    
    def get_genre_type(self):
        self.cursor.execute('SELECT DISTINCT genre FROM genres')
        distinct_genre = self.cursor.fetchall()
        return distinct_genre
    


    def search_movie(self,keywords):
        query =""" SELECT * FROM movies m WHERE MATCH(m.title)
                AGAINST('{}' IN NATURAL LANGUAGE MODE)""".format(keywords)
        self.cursor.execute(query)
        movies = self.cursor.fetchall()
        return movies
    
    def get_tmbdID_from_movieID(self,movieID):
        # search by movie title return tmdb id
        query ="""SELECT DISTINCT m.tmdbId FROM movies m
                \n WHERE m.movie_id = {}""".format(movieID)
        self.cursor.execute(query)
        id = self.cursor.fetchall()

        tmdbID =int(id[0]["tmdbId"])
    
        return tmdbID
    


    
    def close_cursor(self):
        self.cursor.close()
