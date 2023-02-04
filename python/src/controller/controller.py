from model import Model
import json

class Controller:
    def __init__(self)-> None:
        self.model = Model()

    def get_default_data(self):
        data= self.model.get_default_data()
        json_data = json.dumps(data)
        return json_data
    
    def sort_by_date(self):
        data= self.model.sort_by_date()
        json_data = json.dumps(data)
        return json_data
    
    def sort_by_title(self):
        data= self.model.sort_by_title()
        json_data = json.dumps(data)
        return json_data
    
    def get_genre_type(self):
        data = self.model.get_genre_type()
        json_data =json.dumps(data)
        return json_data
    
    def get_film_by_gern(self,genre):
        ## input genre has to be in form of list or tuple
        data = self.model.get_film_by_genre(genre)
        json_data = json.dumps(data)
        return json_data
    