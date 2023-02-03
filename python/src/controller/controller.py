from model import Model
import json

class Controller:
    def __init__(self)-> None:
        self.model = Model()

    def get_default_data(self):
        data= self.model.get_default_data()
        json_data = json.dumps([dict(ix) for ix in data])
        return json_data
    
    def sort_by_date(self):
        data= self.model.sort_by_date()
        json_data = json.dumps(data)
        return json_data
    
    def sort_by_title(self):
        data= self.model.sort_by_title()
        json_data = json.dumps(data)
        return json_data
    
    