import requests
from requests_futures.sessions import FuturesSession
import sys

class TmdbModel():
    def __init__(self) -> None:
        self.API_KEY = '0c7ff4f558bf3a9fa1d8291215717f93'

    def getTmdbMovieData(self, tmdbId):
        tmdbId =[353486,8844]
        lst =[]
        # content ,date ,director,lead actors,rottentotatto
        for x in tmdbId:
            url = "https://api.themoviedb.org/3/movie/{id}?api_key={key}".format(id = x ,key = self.API_KEY)
            url1= "https://api.themoviedb.org/3/movie/{id}?api_key={key}/credits".format(id = x ,key = self.API_KEY)
            data1 = requests.get(url)
            data2 =requests.get(url1)
            data =(data1.json()|data2.json())
            print(data, file=sys.stderr)
            lst.append(data)
        return lst
    
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
