# import mysql.connector
from flask import Flask, request
from controller import Controller
from flask_cors import CORS
import sys

controller =Controller()

app = Flask(__name__)
# Add the CORS header to the json objects to avoid the error
CORS(app)

@app.route('/movies', methods=['GET'])
def get_movies():
    """Get the list of movies with additional filters and sorting from the database.

    Parameters:
        genres (str): A string in the format ["genre"(,"genre")+] corresponding to the genres to be filtered: e.g. ["Adventure", "Family"]
        sort_by (str): A string in the format BY(_DESC)? corresponding to the sorting to be applied e.g. DATE_DESC or RATING
    Returns:
        _type_: _description_
    """
    #Get request parameters
    args = request.args

    date_from = args.get("from")
    date_to = args.get("to")

    min_rating = args.get("min_rating")
    max_rating = args.get("max_rating")

    genres = args.get("genres")

    sort_by = args.get("sortby")
    page = args.get("page")

    return controller.get_movies(genres, date_from, date_to,\
                                                     min_rating, max_rating, sort_by, page)
    


@app.route('/movie', methods=['GET'])
def get_movie_data():
    # args = request.args
    search = 'Jumanji'
    return controller.get_tmdb_data(search)


@app.route('/genres', methods=['GET'])
def get_genres():
    return controller.get_genres()


#@app.after_request
#def after_request(response):
   # response.headers.add('Access-Control-Allow-Origin', '*')
   # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  #  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  #  return response

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=5000)
