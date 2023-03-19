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
                    pool_size = 15,
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
    
    def __exec_query_params(self,query,params): # w params
       cnx = mysql.connector.connect(pool_name = "mypool")
       curs = cnx.cursor(dictionary=True)

       curs.execute(query,params)
       response = curs.fetchall()

       curs.close()
       cnx.close()
       return response 
    
    def __double_exec_query(self, q1,q1_params, q2):
        cnx = mysql.connector.connect(pool_name = "mypool")
        curs = cnx.cursor(dictionary=True)
        print(q1,file=sys.stderr)
        print(q1_params,file=sys.stderr)
        curs.execute(q1,q1_params)
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
        
        q,q_params = self.__gen_movies_query(genres, date_from, date_to, min_rating, max_rating, sort_by, desc, page)
        query_found_rows = "SELECT FOUND_ROWS()"
        return self.__double_exec_query(q,q_params, query_found_rows)


    def __add_pagination(self, page_num):
        
        offset = (int(page_num) - 1) * self.__PAGE_SIZE 

        return "LIMIT %s, %s;",(offset, self.__PAGE_SIZE)
        
    
    def __create_date_filter(self, date_from, date_to):
        if date_from is not None and date_to is not None:
            return 'AND release_date BETWEEN %s AND %s',(date_from,date_to)
        return "",()
        
    def __create_rating_filter(self, min_rating, max_rating):
        if min_rating is not None and max_rating is not None:
            return 'AND r.avg_rating BETWEEN %s AND %s',(min_rating, max_rating)
        return "",()
        
    def __create_genre_filter(self, genres):
        if genres is not None:
            genres = genres.replace('(\'','')
            genres = genres.replace('\')','')
            return 'AND EXISTS (SELECT * FROM genres, movies WHERE m.movie_id = genres.movie_id and genres.genre in (%s))',(genres,)
        return "",()
    def __create_sorting_query(self, sort_by, desc):
        
        if sort_by is not None:

            
            if sort_by == "rating":
                sort_by = "r.avg_rating"
            elif sort_by == "date":
                sort_by = "release_date"
            elif sort_by =="title":
                sort_by = "title"
            else:
                sort_by=""
            
            if desc:
                order = "DESC"
            else:
                order = ""

            
            return 'ORDER BY {0} {1}'.format(sort_by,order),()
            
        return "",()
  
    def __gen_movies_query(self, genres, date_from, date_to, min_rating, max_rating, sort_by, desc, page):
        #TODO add part for rating

        date_filter,params1 = self.__create_date_filter(date_from, date_to)
        genre_filter,params2 = self.__create_genre_filter(genres)
        rating_filter,params3 = self.__create_rating_filter(min_rating, max_rating)
        sorting,params4 = self.__create_sorting_query(sort_by, desc)
        pagination,params5 = self.__add_pagination(page)

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
        params = params1+params2+params3+params4+params5
        print(query, file=sys.stderr)
        print(params, file=sys.stderr)
        return query,params
    
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
                \n AGAINST(%s IN NATURAL LANGUAGE MODE)"""
        return self.__exec_query_params(query,(keywords,))
    
    def get_tmdbID_from_movieID(self, movieID):
        # search by movie title return tmdb id
        query ="""SELECT DISTINCT m.tmdbId FROM movies m
                \n WHERE m.movie_id = %s"""
        id = self.__exec_query_params(query,(movieID,))

        tmdbID =int(id[0]["tmdbId"])
    
        return tmdbID
    
    def get_imdbID_from_movieID(self, movieID):
        query ="""SELECT DISTINCT m.imdbId FROM movies m
                \n WHERE m.movie_id = %s"""
        id = self.__exec_query_params(query,(movieID,))
        imdbID = id[0]["imdbId"]
    
        return imdbID
    
    def get_movie_genre(self,movieID):
        query ='''SELECT DISTINCT g.genre FROM genres g
            \n WHERE g.movie_id = %s'''
        data = self.__exec_query_params(query,(movieID,))
        return data
    
    # Requirement 3:
    def get_catg_filter(self,lo_hi_raters):
        if lo_hi_raters=="high": # if true get the high_raters' avg score for the movie 
            category = "high_raters_avg"
            filter = ">4"
        elif lo_hi_raters=="low":   # get the low_raters' avg score for the movie 
            category = "low_raters_avg"
            filter = "<3.5"
        else:
            filter=""
            category=""

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
                    \nWHERE m.movie_id = %s
                    \nGROUP BY u.user_id
                    \nHAVING u.avg_rating{0})
                    \nSELECT CONVERT(AVG(u_avg_for_movie),float) AS {1}
                    \nFROM user_ratings""".format(filter,category)     

        return self.__exec_query_params(query,(movieId,))
    

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
                    \nWHERE m.movie_id = %s
                    \nHAVING u.u_avg_for_genre{0})
                    \nSELECT genre, CONVERT(AVG(u_avg_for_movie), float) AS {1}
                    \nFROM user_ratings
                    \nGROUP BY genre
                    \nORDER BY genre""".format(filter, category)
         
        return self.__exec_query_params(query,(movieId,))

    
    # Requirement 4:

    # Explore relationship between tag data and rating
    # Display average ratings for movies with different tags 
    # If tag is not in db, return empty list
    def tags_rating(self,movie_id):
        query_tags ="""SELECT DISTINCT tags.tag 
                      \n FROM movies 
                      \n JOIN tags ON movies.movie_id = tags.movie_id 
                      \n WHERE movies.movie_id = %s"""
        tags_movie =  self.__exec_query_params(query_tags,(movie_id,))

        query_rating = """SELECT t.tag, CONVERT(AVG(avg_rating),float) AS overall_average_rating
                \n FROM(SELECT r.movie_id, CONVERT(AVG(r.rating),float) AS avg_rating
                \nFROM ratings r
                \nJOIN tags t ON r.movie_id = t.movie_id
                \nWHERE t.tag = %s   
                \nGROUP BY r.movie_id) AS subq
                \nJOIN tags t ON subq.movie_id = t.movie_id
                \nWHERE t.tag = %s
                \nGROUP BY t.tag""" 

        for tag in tags_movie:
            tag['rating']= self.__exec_query_params(query_rating,(tag['tag'],tag['tag']))[0]['overall_average_rating']
        # print(tags_movie,file=sys.stderr)
       

        return tags_movie
    
    # Explore relationship between tag data and genres
    # Display all the tags associated with a genre
    def genre_tags(self,genre):
        query="""SELECT t.tag, COUNT(t.tag) AS n_tags
                \nFROM tags t
                \nJOIN genres g ON g.movie_id = t.movie_id
                \nWHERE g.genre = %s
                \nGROUP BY t.tag"""

        return self.__exec_query_params(query,(genre,))
    
    # Do individual viewers apply the same tags to different films in the same genre?

    # get the genre list
    def get_genre_list(self):
        query="""SELECT DISTINCT g.genre FROM genres g"""
        return self.__exec_query(query)
    
    # get the tag list
    def get_tag_list(self, n_tags):
        query="""SELECT DISTINCT t.tag FROM tags t LIMIT %s"""
        
        return self.__exec_query_params(query,(int(n_tags),))
    

    #Get % of movies within the same genre that share this tag.
    def perc_w_tag(self,genre,tag):
        query="""SELECT  CONVERT(COUNT(DISTINCT g.movie_id)/ 
                \n( SELECT COUNT(DISTINCT genres.movie_id) FROM genres WHERE genre = %s) * 100,float) AS perc_w_tag
                \nFROM genres g
                \nINNER JOIN tags t ON g.movie_id = t.movie_id
                \nWHERE g.genre = %s AND t.tag = %s """
               
        return self.__exec_query_params(query,(genre,genre,tag))
    
    # get the data for the heatmap
    def get_most_occur(self):
        query ="""SELECT t.tag
                    FROM genres g
                    JOIN tags t ON g.movie_id = t.movie_id
                    GROUP BY t.tag
                    ORDER BY COUNT(*) DESC
                    LIMIT 25;
                    """
        res=[]
        genres = self.get_genre_list()
        genres.pop(len(genres)-1) # remove (no genres listed)  
        # print(genres,file=sys.stderr)
        
        for g in genres:
            genre=g['genre']
            # print(genre,file=sys.stderr)

            tags = self.__exec_query(query)
            # print(tags,file=sys.stderr)

            for tag in tags:
                tag['genre']=genre
                tag['percentage'] = (self.perc_w_tag(genre,tag['tag'])[0]['perc_w_tag'])
            res=res+tags

        return res
    
    
        
  
    ## Requirement 5:
    # generate number of preview audience and Actual average rating
    def gen_num_audience(self,movieID):
        query =''' SELECT COUNT(DISTINCT(r.user_id)) As num_rater, CONVERT(AVG(rating),float) AS overall_average_rating
                \n FROM ratings r
                \n WHERE r.movie_id =%s'''
        data = self.__exec_query_params(query,(movieID,))
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
            pred = [{'Predicted Rating':prediction},{'Actual Average Rating':True_average_rating}, {'nb_raters': num_Total_rater}]
            return pred
        num_audience = num_Total_rater//4
        if threshold =='':
            threshold =2
        query ='''
            SELECT AVG(r.rating) as predicted_rating,STDDEV(r.rating) as STD
            FROM
            (SELECT CONVERT(r.rating, float) AS rating
            \n FROM ratings r
            \n WHERE r.movie_id =%s
            \n ORDER BY RAND()
            \n LIMIT %s)r
            WHERE r.rating BETWEEN  (
                SELECT AVG(a.rating) - %s*STDDEV(a.rating)
                    FROM ratings a
                    WHERE movie_id = %s
                    ORDER BY RAND()
                    LIMIT %s)
                 AND (
                    SELECT AVG(a.rating) + %s*STDDEV(a.rating)
                    FROM ratings a
                    WHERE movie_id = %s
                    ORDER BY RAND()
                    LIMIT %s) '''        
        data =self.__exec_query_params(query,(movieID,num_audience,threshold,movieID,num_audience,threshold,movieID,num_audience))
        data.append({'True_average_rating':True_average_rating})
        data.append({'nb_preview_raters': num_audience})
        data.append({'nb_raters': num_Total_rater})
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

        query = """\nSELECT AVG(pr.rating) as %s
                    \nFROM personality p, personalityRating pr
                    \nWHERE p.userid = pr.userid
                    \nAND pr.movie_id = %s
                    \nAND p.%s %s"""
        
        
        personality_avg_rating = self.__exec_query_params(query,(personality,movieId,personality,filter))
        return personality_avg_rating

    # Q6.2
    def gen_personality_genre_data(self,f,genre):
        # FOR each genre type, Get average personality traits who rated this genre highly/lowly
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
                \n WHERE g.genre = '%s' 
                \n group by p.userid 
                \n %s AND count > 30)t
                group by t.genre'''
        print(query, file=sys.stderr)
        data = self.__exec_query_params(query,(genre,filter))
        return data
        # For each ppl who scored high in one personality traits , select their favorate film
    def gen_fav_for_all_personality(self):
        Personality =['openness', 'agreeableness', 'emotional_stability', 'conscientiousness', 'extraversion']
        data =[]
        for p in Personality:
            attribute ={'attribute':f'high {p}'}
            d =self.gen_fav_genre_by_peronslity(p)
            for x in d :
                x |= attribute
                data.append(x)
        
        return data
    def gen_fav_genre_by_peronslity(self,personality):

    
        # query3 ='''
        #         SELECT z.genre,COUNT(z.genre) as count
        #         FROM(
        #         (SELECT MAX(m.num)as numRated,m.userid
        #             FROM(
        #             SELECT pt.userid,g.genre as genre,COUNT(pr.movie_id) as num
        #             FROM personality pt 
        #             INNER JOIN personalityRating pr on pt.userid = pr.userid AND pt.{0} >5 AND {1}
        #             INNER JOIN genres g on g.movie_id = pr.movie_id
        #             GROUP BY genre, pt.userid)m
        #         GROUP BY m.userid
        #         ORDER BY numRated DESC)a

        #         JOIN (SELECT pt.userid,g.genre as genre,COUNT(pr.movie_id) as number
        #             FROM personality pt 
        #             INNER JOIN personalityRating pr on pt.userid = pr.userid AND pt.{0} >5 AND {1}
        #             INNER JOIN genres g on g.movie_id = pr.movie_id
        #             GROUP BY genre, pt.userid)z on z.userid = a.userid and z.number = a.numRated)

        #         GROUP BY z.genre
        #         ORDER BY count DESC

        # '''.format(personality,'pr.rating >4') 
        #
        query3 ='''
                SELECT g.genre as genre , AVG(pr.rating) as averageRating
                FROM personalityRating pr 
                INNER JOIN personality pt on pt.userid = pr.userid AND pt.%s>5
                INNER JOIN genres g on pr.movie_id = g.movie_id
                GROUP BY g.genre'''                                  
                    
        data = self.__exec_query_params(query3,(personality,))

        return data

    

    def close_cursor(self):
        self.cursor.close()
