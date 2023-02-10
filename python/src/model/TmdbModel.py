import requests
from requests_futures.sessions import FuturesSession

class TmdbModel():
    def __init__(self) -> None:
        self.API_KEY = 'fakeapikey'

    def getTmdbMovieData(self, movieID):
        url = "https://api.themoviedb.org/3/movie/{id}?api_key={key}".format(id = movieID, key = self.API_KEY)
        data = requests.get(url)
        return data.json()
    def getTmdbUrls(self, results):
        return


    def addImgPathToResults(self, results):
        
        urls = []
        #TODO: if it doesnt work, error handling + json for the requests
        with FuturesSession() as session:
            futures = [session.get("https://api.themoviedb.org/3/movie/{id}?api_key={key}".format(id = result["tmdbId"], key = self.API_KEY)) for result in results]
            

            for i in range(len(results)):
                results[i]["imgPath"] = "https://image.tmdb.org/t/p/w500{path}?api_key={key}".format(path= futures[i]["poster_path"], key = self.API_KEY)
            

        print(results[0])
        return results
