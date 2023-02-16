from model import Model
from TmdbModel import TmdbModel
import json

class Controller:
    def __init__(self)-> None:
        self.model = Model()
        self.tmdbModel = TmdbModel()

    def get_genre_type(self):
        data = self.model.get_genre_type()
        json_data =json.dumps(data)
        return json_data
    
    def get_film_by_genre_date_rating(self,genre,date_start,date_end,rating_min,rating_max,sort_by_date,sort_by_title,sort_by_rating,page):
        ## input genre has to be in form of list or tuple
        data = self.model.get_film_by_genre_date_rating(genre,date_start,date_end,rating_min,rating_max,sort_by_date,sort_by_title,sort_by_rating,page)
        json_data = json.dumps(data)
        return json_data

    def get_tmdb_data(self,keyword):
        tmdbID =self.get_tmdbID(keyword)
        return self.tmdbModel.getTmdbMovieData(tmdbID )
    
    def get_tmdbID(self,keyword):
        # get tmdb ID from movie title
        data = self.model.search_tmbdID(keyword)
        json_data = json.dumps(data)
        return(json_data)

    
   
