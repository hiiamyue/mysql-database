from model import Model
from TmdbModel import TmdbModel
import json
import sys
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
            
        data = self.model.get_movies(genres, date_from, date_to, min_rating, max_rating, sort_by, desc)
        json_data = json.dumps(data)
        return json_data

    def get_movie_data(self, movie_id):
        data = json.dumps(self.tmdbModel.getTmdbMovieData(movie_id))
        
        return data

    def get_tmdb_data(self,keyword):
        tmdbID =self.get_tmdbID(keyword)
        return self.tmdbModel.getTmdbMovieData(tmdbID )
    
    def get_tmdbID(self,keyword):
        # get tmdb ID from movie title
        data = self.model.search_tmbdID(keyword)
        json_data = json.dumps(data)
        return(json_data)

    
   
