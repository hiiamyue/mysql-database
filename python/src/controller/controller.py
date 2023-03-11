from model import Model
from TmdbModel import TmdbModel
import json
import sys
from math import ceil

class Controller:
    def __init__(self)-> None:
        self.model = Model()
        self.tmdbModel = TmdbModel()

    def get_genre_type(self):
        data = self.model.get_genre_type()
        json_data =json.dumps(data)
        return json_data
    
    def get_movies(self, genres, date_from, date_to, min_rating, max_rating, sort_by, page):
        
        # Parse the sorting method
        if sort_by is not None:
            desc = len(sort_by.split("_")) == 2
            sort_by = sort_by.split("_")[0]
            
        else: 
            desc = None

        if page == None:
            page = 1
            
        # Compute the payload:
        payload = {}   

        results = self.model.get_movies(genres, date_from, date_to, min_rating, max_rating, sort_by, desc, page)
        payload["results"] = self.tmdbModel.addImgPathToResults(results)

        total_rows = self.model.get_last_query_found_rows()
        payload["pagination"] = {"page_number": page, 'total_results': total_rows[0]['FOUND_ROWS()'], "max_page": ceil(total_rows[0]['FOUND_ROWS()']/self.model.get_page_size())}

        json_data = json.dumps(payload)
        return json_data

    # def get_movie_data(self, movie_id):
    #     data = json.dumps(self.tmdbModel.getTmdbMovieData(movie_id))
    #     return data
    def search_movie(self,keyword):
        data = self.tmdbModel.addImgPathToResults(self.model.search_movie(keyword))
        json_data =json.dumps(data)
        return json_data
    

    def get_tmdb_data(self,movieID):
        tmdbID =self.get_tmdbID(movieID)
        tmdbData =self.tmdbModel.getTmdbMovieData(tmdbID)
        preview_rating = self.predict(movieID)
        data =preview_rating | tmdbData
        return json.dumps(data)
    
    def get_rotten_tomatoes_rating(self, movieID):
        imdbID = self.get_imdbID(movieID)
        return self.tmdbModel.get_rotten_tomatoes_rating(imdbID)
    
    def get_tmdbID(self,movieID):
        # get tmdb ID from movie title
        data = self.model.get_tmdbID_from_movieID(movieID)
        json_data = json.dumps(data)
        return(json_data)
    
    def get_imdbID(self, movieID):
        # get tmdb ID from movie title
        data = self.model.get_imdbID_from_movieID(movieID)
        json_data = json.dumps(data)
        return(json_data)

    def get_reaction(self,movieID, lo_hi_raters):
        data = self.model.get_group_rating(movieID, lo_hi_raters)
        json_data = json.dumps(data)
        return json_data
    
    def get_reaction_genre(self, movieId, lo_hi_raters):
        data = self.model.get_group_rating_genre(movieId, lo_hi_raters)
        json_data = json.dumps(data)
        return json_data
    
    def get_tags_rating(self,tag):
        data = self.model.tags_rating(tag)
        json_data = json.dumps(data)
        return json_data
    
    def get_genre_tags(self,genre):
        data = self.model.genre_tags(genre)
        json_data = json.dumps(data)
        return json_data
   
    def user_tag_analysis(self,page,genre_filter):
        data = self.model.user_tag_analysis(page,genre_filter)
        json_data = json.dumps(data)
        return json_data
    
    def genre_list(self):
        genres_data = self.model.get_genre_list()
        genres =[]
        for entry in genres_data:
            if entry["genre"]!="(no genres listed)":
                genres.append(entry["genre"])
        return genres
    def tags_list(self,n_tags):
        tags_data = self.model.get_tag_list(n_tags)
        tags = []
        for entry in tags_data:
                tags.append(entry["tag"])
        return tags
    def perc_w_tag(self,genre,tag):
        data = self.model.perc_w_tag(genre,tag)
        json_data = json.dumps(data)
        return json_data

      
    def predict(self,movieID):
        data =self.model.gen_prediction(movieID)
        return data
    
    def QuestionSix(self):
        data = self.model.personal()
        return data

