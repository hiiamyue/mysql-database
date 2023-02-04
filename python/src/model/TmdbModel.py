import requests

class TmdbModel():
    def __init__(self) -> None:
        self.API_KEY = 'fakeapikey'

    def getTmdbMovieData(self, movieID):
        url = "https://api.themoviedb.org/3/movie/{id}?api_key={key}".format(id = movieID, key = self.API_KEY)
        data = requests.get(url)
        return data.json()