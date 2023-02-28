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
    
    def get_page_size(self):
        return self.__PAGE_SIZE

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
        
        
        
        offset = (int(page_num) - 1) * self.__PAGE_SIZE 

        return "LIMIT {0}, {1};".format(str(offset), self.__PAGE_SIZE)
        
    
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
    
    # Requirement 3:
    def get_catg_filter(self,lo_hi_raters):
        if lo_hi_raters=="high": # if true get the high_raters' avg score for the movie 
            category = "high_raters_avg"
            filter = "HAVING u.avg_rating>4"
        elif lo_hi_raters=="low":   # get the low_raters' avg score for the movie 
            category = "low_raters_avg"
            filter = "HAVING u.avg_rating<3.5"

        return filter,category
    
    # Get the relevant group's rating for the movie
    def get_group_rating(self,movieId, lo_hi_raters):
        filter,category = self.get_catg_filter(lo_hi_raters)
   
        query = """\nWITH user_ratings AS (
                    \nSELECT u.user_id, u.avg_rating, rating AS u_avg_for_movie
                    \nFROM (SELECT user_id, CONVERT(AVG(rating), float) AS avg_rating
                    \nFROM ratings GROUP BY user_id) u
                    \nINNER JOIN ratings r ON r.user_id = u.user_id
                    \nINNER JOIN movies m ON r.movie_id = m.movie_id
                    \nWHERE m.movie_id = {0}
                    \nGROUP BY u.user_id
                    \n{1})
                    \nSELECT CONVERT(AVG(u_avg_for_movie),float) AS {2}
                    \nFROM user_ratings""".format(movieId,filter,category)     

        self.cursor.execute(query)
        u_avg_rating = self.cursor.fetchall()
        return u_avg_rating
    
    # Requirement 4:

    # Explore relationship between tag data and rating
    # Display average ratings for movies with different tags 
    # If tag is not in db, return empty list
    def tags_rating(self,tag):
        query = """SELECT t.tag, CONVERT(AVG(avg_rating),float) AS overall_average_rating
                   \n FROM(SELECT r.movie_id, CONVERT(AVG(r.rating),float) AS avg_rating
                   \nFROM ratings r
                   \nJOIN tags t ON r.movie_id = t.movie_id
                   \nWHERE t.tag = \'{0}\'   
                   \nGROUP BY r.movie_id) AS subq
                   \nJOIN tags t ON subq.movie_id = t.movie_id
                   \nWHERE t.tag = \'{0}\' 
                   \nGROUP BY t.tag""".format(tag,tag)    

        self.cursor.execute(query)
        tag_avg_rating = self.cursor.fetchall()
        return tag_avg_rating
    
    # Explore relationship between tag data and genres
    # Display all the tags associated with a genre
    # Maybe worth to add pagination here?
    def genre_tags(self,genre):
        query="""SELECT t.tag
                \nFROM tags t
                \nJOIN genres g ON g.movie_id = t.movie_id
                \nWHERE g.genre = \'{}\'""".format(genre)

        self.cursor.execute(query)
        genre_tags = self.cursor.fetchall()
        return genre_tags
    
    # Do individual viewers apply the same tags to different films?
    def user_tag_analysis(self,page,genre_filter=None):
        filter=""
        pagination = self.__add_pagination(page)
        # Optional additional filter
        # Do individual viewers apply the same tags to different films in the same genre?
        if genre_filter:
            filter = """\nJOIN genres g ON t.movie_id = g.movie_id
                        \n JOIN genres g1 ON t1.movie_id = g1.movie_id AND g.genre = g1.genre"""
        query="""SELECT DISTINCT t.user_id, t.movie_id, t.tag, t1.movie_id, t1.tag
                    \nFROM tags t
                    \nJOIN tags t1 ON 
                    \nt.user_id = t1.user_id AND t.tag = t1.tag AND t.movie_id != t1.movie_id
                    \n{0}
                    \n{1}""".format(filter,pagination)

      
            
        self.cursor.execute(query)
        genre_tags = self.cursor.fetchall()
        return genre_tags
    
    
    def close_cursor(self):
        self.cursor.close()
