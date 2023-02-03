from model import Model
import json

class Controller:
    def __init__(self)-> None:
        self.model = Model()

    def get_default_data(self):
        data= self.model.get_default_data()
        json_data=[]
        for movie in data:
            json_obj ={"movieId":movie[0], "title":movie[1],"release_date":movie[2],\
                       "imdbId":movie[3],"tmdbId":movie[4]}
            json_data.append(json_obj)
        return json_data
    
    def sort_by_date(self):
        data= self.model.sort_by_date()
        json_data=[]
        for movie in data:
            json_obj ={"movieId":movie[0], "title":movie[1],"release_date":movie[2],\
                       "imdbId":movie[3],"tmdbId":movie[4]}
            json_data.append(json_obj)
        return json_data
    
    def sort_by_title(self):
        data= self.model.sort_by_title()
        json_data=[]
        for movie in data:
            json_obj ={"movieId":movie[0], "title":movie[1],"release_date":movie[2],\
                       "imdbId":movie[3],"tmdbId":movie[4]}
            json_data.append(json_obj)
        return json_data
    
    def sort_by_rating(self):
        data= self.model.sort_by_rating()
        json_data=[]
        for movie in data:
            json_obj ={"movieId":movie[0], "title":movie[1],"release_date":movie[2],\
                       "imdbId":movie[3],"tmdbId":movie[4]}
            json_data.append(json_obj)
        return json_data
    
    
    