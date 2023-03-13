import requests
from requests_futures.sessions import FuturesSession
import sys
import json

#TODO: Add rotten tomato rating, catch error , maybe edit variable names
class TmdbModel():
    def __init__(self) -> None:
        self.API_KEY = '0c7ff4f558bf3a9fa1d8291215717f93'
        self.OMDB_API_KEY = "591bee91"

    def getTmdbMovieData(self, tmdbId):
        dic ={}
        dic2={'cast':[],'director':[]}
        # content ,date ,director,lead actors,rottentotatto
        url = "https://api.themoviedb.org/3/movie/{id}?api_key={key}".format(id = tmdbId ,key = self.API_KEY)
        url1= "https://api.themoviedb.org/3/movie/{id}/credits?api_key={key}".format(id = tmdbId ,key = self.API_KEY)
        data1 = requests.get(url)
        data2 =requests.get(url1)
        keys = ['title','adult','homepage','original_language','overview','release_date','runtime','poster_path']
       
        for item in data1.json():
            if item in keys:
                dic[item] = data1.json()[item]
        for p in data2.json():
            if p =='cast':
                for z in data2.json()[p]:
                    if z['order']<= 5:
                        actor = {'character':z['character'],'name':z['name']}
                        dic2['cast'].append(actor)
                    else:
                        break
            if p =='crew':
                for j in data2.json()[p]:
                    if j['job']=="Director":
                        director ={'name':j['name']}
                        dic2['director'].append(director)
                        break
        dic |= dic2
        print(dic, file=sys.stderr)
        return dic
    
    def getTmdbUrls(self, results):
        return

    def addImgPathToResults(self, results):
        urls = []
        #TODO: if it doesnt work, error handling + json for the requests
        with FuturesSession() as session:
            futures = [session.get("https://api.themoviedb.org/3/movie/{id}?api_key={key}".format(id = result["tmdbId"], key = self.API_KEY)) for result in results]
            

            for i in range(len(results)):
                try:
                    results[i]["imgPath"] = "https://image.tmdb.org/t/p/w500{path}?api_key={key}".format(path= json.loads(futures[i].result().content)["poster_path"], key = self.API_KEY)
                except KeyError:
                     results[i]["imgPath"] = "null"
        return results
    
    def get_rotten_tomatoes_rating(self, imdbId):
        imdbId = imdbId[1:-1]
        url = f"http://www.omdbapi.com/?apikey={self.OMDB_API_KEY}&i=tt{imdbId}"
        data = requests.get(url).json()
        ratings = data["Ratings"]
        
        for source in ratings:
            if source["Source"] == "Rotten Tomatoes":
                return source["Value"]
            
        return "N/A"
    