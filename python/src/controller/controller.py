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
        payload["results"] = results

        total_rows = self.model.get_last_query_found_rows()
        payload["pagination"] = {"page_number": page, 'total_results': total_rows[0]['FOUND_ROWS()'], "max_page": ceil(total_rows[0]['FOUND_ROWS()']/self.model.get_page_size())}

        json_data = json.dumps(payload)
        return json_data

    # def get_movie_data(self, movie_id):
    #     data = json.dumps(self.tmdbModel.getTmdbMovieData(movie_id))
    #     return data
    def search_movie(self,keyword):
        data =self.model.search_movie(keyword)
        json_data =json.dumps(data)
        print(json_data, file=sys.stderr)
        return json_data
    

    def get_tmdb_data(self,movieID):
        tmdbID =self.get_tmdbID(movieID)
        return self.tmdbModel.getTmdbMovieData(tmdbID)
    
    def get_tmdbID(self,movieID):
        # get tmdb ID from movie title
        data = self.model.get_tmbdID_from_movieID(movieID)
        json_data = json.dumps(data)
        return(json_data)

    def get_reaction(self,movieID, lo_hi_raters):
        data = self.model.get_group_rating(movieID, lo_hi_raters)
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
