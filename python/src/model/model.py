import mysql.connector
import time
import sys
import re
import numpy
import os

class Model:
    
    def __init__(self) -> None:
        while True:
            try:
                mydb = mysql.connector.connect(
                    pool_name = "mypool",
                    pool_size = 10,
                    host="mysql",
                    user="root",
                    password=os.environ.get('DB_PASS',''),
                    database="db",
                    sql_mode = ''
                )
                
                break
            except:
                print("-")
                time.sleep(1)

        self.db = mydb
        self.cursor = self.db.cursor(dictionary=True)
        #self.cursor.execute('set global max_allowed_packet=67108864')
    
        self.__PAGE_SIZE = 28
    
    def get_page_size(self):
        return self.__PAGE_SIZE
    
    def __exec_query(self, query):
        cnx = mysql.connector.connect(pool_name = "mypool")
        curs = cnx.cursor(dictionary=True)

        curs.execute(query)
        response = curs.fetchall()

        curs.close()
        cnx.close()
        return response
    
    def __double_exec_query(self, q1, q2):
        cnx = mysql.connector.connect(pool_name = "mypool")
        curs = cnx.cursor(dictionary=True)

        curs.execute(q1)
        response = [curs.fetchall()]
        curs.execute(q2)
        response.append(curs.fetchall())
        print(response, file=sys.stderr)
        curs.close()
        cnx.close()
        return response

    

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
        query_found_rows = "SELECT FOUND_ROWS()"
        return self.__double_exec_query(q, query_found_rows)


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
            if sort_by == "date":
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
        """_summary_

        Returns:
            _type_: _description_
        """
        query = "SELECT DISTINCT genre, DENSE_RANK() OVER(ORDER BY genre) as id FROM genres WHERE genre != '(no genres listed)' ORDER BY genre"
        return self.__exec_query(query)
    


    def search_movie(self,keywords):
        
        query =""" SELECT DISTINCT * FROM movies m 
                 \n INNER JOIN ( SELECT CONVERT(AVG(rating), float) AS avg_rating, movie_id
                \n FROM ratings 
                \n group by movie_id
                )r on m.movie_id = r.movie_id
                \n WHERE MATCH(m.title)
                \n AGAINST('{}' IN NATURAL LANGUAGE MODE)
                
                """.format(keywords)
        return self.__exec_query(query)
    
    def get_tmdbID_from_movieID(self, movieID):
        # search by movie title return tmdb id
        query ="""SELECT DISTINCT m.tmdbId FROM movies m
                \n WHERE m.movie_id = {}""".format(movieID)
        self.cursor.execute(query)
        id = self.cursor.fetchall()

        tmdbID =int(id[0]["tmdbId"])
    
        return tmdbID
    
    def get_imdbID_from_movieID(self, movieID):
        query ="""SELECT DISTINCT m.imdbId FROM movies m
                \n WHERE m.movie_id = {}""".format(movieID)
        self.cursor.execute(query)
        id = self.cursor.fetchall()
        imdbID = id[0]["imdbId"]
    
        return imdbID
    def get_movie_genre(self,movieID):
        query ='''SELECT DISTINCT g.genre FROM genres g
            \n WHERE g.movie_id = {}'''.format(movieID)
        data = self.__exec_query(query)
        return data
    
    # Requirement 3:
    def get_catg_filter(self,lo_hi_raters):
        if lo_hi_raters=="high": # if true get the high_raters' avg score for the movie 
            category = "high_raters_avg"
            filter = ">4"
        elif lo_hi_raters=="low":   # get the low_raters' avg score for the movie 
            category = "low_raters_avg"
            filter = "<3.5"

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
                    \nHAVING u.avg_rating{1})
                    \nSELECT CONVERT(AVG(u_avg_for_movie),float) AS {2}
                    \nFROM user_ratings""".format(movieId,filter,category)     

        self.cursor.execute(query)
        u_avg_rating = self.cursor.fetchall()
        return u_avg_rating
    

    def get_group_rating_genre(self, movieId, lo_hi_raters):
        # For each genre, return the average rating of a movie given by people who rate that genre highly or lowly.
        # Example: People who rate comedy films highly give this movie an average rating of 4.0
        filter, category = self.get_catg_filter(lo_hi_raters)
        
        query = """\nWITH user_ratings AS (
                    \nSELECT u.user_id, u.u_avg_for_genre, genre, rating AS u_avg_for_movie
                    \nFROM (
                    \nSELECT user_id, CONVERT(AVG(rating), float) AS u_avg_for_genre, genre
                    \nFROM ratings, genres
                    \nWHERE ratings.movie_id = genres.movie_id
                    \nGROUP BY user_id, genre) u
                    \nINNER JOIN ratings r ON r.user_id = u.user_id
                    \nINNER JOIN movies m ON r.movie_id = m.movie_id
                    \nWHERE m.movie_id = {0}
                    \nHAVING u.u_avg_for_genre{1})
                    \nSELECT genre, CONVERT(AVG(u_avg_for_movie), float) AS {2}
                    \nFROM user_ratings
                    \nGROUP BY genre
                    \nORDER BY genre""".format(movieId, filter, category)
         
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
    def genre_tags(self,genre):
        query="""SELECT t.tag, COUNT(t.tag) AS n_tags
                \nFROM tags t
                \nJOIN genres g ON g.movie_id = t.movie_id
                \nWHERE g.genre = \'{}\'
                \nGROUP BY t.tag""".format(genre)

        self.cursor.execute(query)
        genre_tags = self.cursor.fetchall()
        return genre_tags
    
    # Do individual viewers apply the same tags to different films in the same genre?

    # get the genre list
    def get_genre_list(self):
        query="""SELECT DISTINCT g.genre FROM genres g"""
        
        self.cursor.execute(query)
        genre_list = self.cursor.fetchall()
        return genre_list
    
    # get the tag list
    def get_tag_list(self, n_tags):
        query="""SELECT DISTINCT t.tag FROM tags t LIMIT {}""".format(n_tags)
        
        self.cursor.execute(query)
        tag_list = self.cursor.fetchall()
        return tag_list
    
    #Get % of movies within the same genre that share this tag.
    def perc_w_tag(self,genre,tag):
        query="""SELECT  CONVERT(COUNT(DISTINCT g.movie_id)/ 
                \n( SELECT COUNT(DISTINCT genres.movie_id) FROM genres WHERE genre = \'{0}\') * 100,float) AS perc_w_tag
                \nFROM genres g
                \nINNER JOIN tags t ON g.movie_id = t.movie_id
                \nWHERE g.genre = \'{0}\' AND t.tag = \'{1}\' """.format(genre,tag)
               
        
        self.cursor.execute(query)
        perc_with_tag = self.cursor.fetchall()
        return perc_with_tag
        
  
    ## Requirement 5:
    # generate number of preview audience and Actual average rating
    def gen_num_audience(self,movieID):
        query =''' SELECT COUNT(DISTINCT(r.user_id)) As num_rater, CONVERT(AVG(rating),float) AS overall_average_rating
                \n FROM ratings r
                \n WHERE r.movie_id ={}
                
        '''.format(movieID)
        data = self.__exec_query(query)
        try:
            num_Total_rater = data[0]['num_rater']
            overall_average_rating =data[0]['overall_average_rating']
        except KeyError:
            num_Total_rater = ''
            overall_average_rating =''
        print(num_Total_rater, file=sys.stderr)

        return num_Total_rater,overall_average_rating
    
    # randomly pick number of preview ratings and remove outliers that is not within 1 standard deviation
    def gen_prediction(self,movieID,threshold):
        num_Total_rater,True_average_rating = self.gen_num_audience(movieID)
        if  num_Total_rater< 30:
            prediction = ''
            dic ={'Predicted Rating':prediction,'Actual Average Rating':True_average_rating}
            return  dic
        num_audience = num_Total_rater//4
        if threshold =='':
            threshold =2
        query ='''
            SELECT AVG(r.rating) as predicted_rating,STDDEV(r.rating) as STD
            FROM
            (SELECT CONVERT(r.rating, float) AS rating
            \n FROM ratings r
            \n WHERE r.movie_id ={0}
            \n ORDER BY RAND()
            \n LIMIT {1})r
            WHERE r.rating BETWEEN  (
                SELECT AVG(a.rating) - {2}*STDDEV(a.rating)
                    FROM ratings a
                    WHERE movie_id = {0} 
                    ORDER BY RAND()
                    LIMIT {1})
                 AND (
                    SELECT AVG(a.rating) + {2}*STDDEV(a.rating)
                    FROM ratings a
                    WHERE movie_id = {0}
                    ORDER BY RAND()
                    LIMIT {1}) 
                
        '''.format(movieID,num_audience,threshold)
        data =self.__exec_query(query)
        data.append({'True_average_rating':True_average_rating})
        data.append({'Number_of_preview_rater over total':f'{num_audience} over {num_Total_rater}'})
        data.append({'threshold':threshold })
        print(data,file=sys.stderr)
        return  data

    # Q6.1
    # For each personality trait, return the average rating of a movie given by people who have a high or low score in that personality trait.
    # Example: People who are extrovert give this movie an average rating of 4.0
    def get_avg_rating_for_all_personality(self, movieId, lo_hi_raters):
        all_personality_avg_rating = []
        for personality in ['openness', 'agreeableness', 'emotional_stability', 'conscientiousness', 'extraversion']:
            all_personality_avg_rating.append(self.get_avg_rating_for_personality(movieId, personality, lo_hi_raters)[0])
        return all_personality_avg_rating

    def get_avg_rating_for_personality(self, movieId, personality, lo_hi_raters):
        filter = ""
        if (lo_hi_raters == "high"):
            filter = ">=4"
        if(lo_hi_raters == "low"):
            filter = "<=2"
        query = f"""\nSELECT AVG(pr.rating) as avg_rating_for_{personality}
                    \nFROM personality p, personalityRating pr
                    \nWHERE p.userid = pr.userid
                    \nAND pr.movie_id = {movieId}
                    \nAND p.{personality} {filter}
                """
        
        self.cursor.execute(query)
        personality_avg_rating = self.cursor.fetchall()
        return personality_avg_rating

    # Q6.2
    def gen_personality_genre_data(self,f,genre):
        # FOR each genre type, Get average personality traits who rated this genre highly
        filter = ''
        if (f == 'high'):
            filter = 'HAVING AVG_rating > 4'
        if(f=='low'):
            filter =' HAVING AVG_rating <2'

        query ='''SELECT t.genre,AVG(t.openness) AS openness ,AVG(t.agreeableness) AS agreeableness ,AVG(t.emotional_stability) AS emotional_stability,AVG(t.conscientiousness) AS conscientiousness,AVG(t.extraversion) AS extraversion
                \n FROM(
                    SELECT DISTINCT p.userid,pt.openness,pt.agreeableness, pt.emotional_stability, pt.conscientiousness, pt.extraversion,g.genre,AVG(p.rating) AS AVG_rating, COUNT(p.rating) AS count
                \n FROM personalityRating p 
                \n INNER JOIN genres g on g.movie_id = p.movie_id
                \n INNER JOIN personality pt on pt.userid = p.userid
                \n WHERE g.genre = '{0}' 
                \n group by p.userid 
                \n {1} AND count > 30)t
                group by t.genre
                '''.format(genre,filter)
       
        data = self.__exec_query(query)
        return data
        # For each ppl who scored high in one personality traits , select their favorate film
    def gen_fav_for_all_personality(self,f):
        Personality =['openness', 'agreeableness', 'emotional_stability', 'conscientiousness', 'extraversion']
        data =[]
        for p in Personality:
            d =self.gen_fav_genre_by_peronslity(f,p)
            data.append({p:d})
        return data
    def gen_fav_genre_by_peronslity(self,f,personality):

        filter2 =''
        if (f == 'high'):
            filter2 ='pr.rating >4'
        if(f=='low'):
            filter2 ='pr.rating <2'
    
        query3 ='''
                SELECT z.genre,COUNT(z.genre) as count
                FROM(
                (SELECT MAX(m.num)as numRated,m.userid
                    FROM(
                    SELECT pt.userid,g.genre as genre,COUNT(pr.movie_id) as num
                    FROM personality pt 
                    INNER JOIN personalityRating pr on pt.userid = pr.userid AND pt.{0} >5 AND {1}
                    INNER JOIN genres g on g.movie_id = pr.movie_id
                    GROUP BY genre, pt.userid)m
                GROUP BY m.userid
                ORDER BY numRated DESC)a

                JOIN (SELECT pt.userid,g.genre as genre,COUNT(pr.movie_id) as number
                    FROM personality pt 
                    INNER JOIN personalityRating pr on pt.userid = pr.userid AND pt.{0} >5 AND {1}
                    INNER JOIN genres g on g.movie_id = pr.movie_id
                    GROUP BY genre, pt.userid)z on z.userid = a.userid and z.number = a.numRated)

                GROUP BY z.genre
                ORDER BY count DESC

        '''.format(personality,filter2)                                        
                    
        data = self.__exec_query(query3)

        return data

    

    def close_cursor(self):
        self.cursor.close()
