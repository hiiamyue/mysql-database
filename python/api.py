# import mysql.connector
from flask import Flask, request
from controller import Controller
from flask_cors import CORS
import sys

controller =Controller()

app = Flask(__name__)
# Add the CORS header to the json objects to avoid the error


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
    
# @app.route('/test', methods=['GET'])
# def test():
#     lis =[]
#     for x in range (1,50):
#         lis.append(controller.predict(x))
#     return lis


@app.route('/movie', methods=['GET'])
def get_movie_data():

    args = request.args
    movie_id = args.get("movie_id")
    
    return controller.get_tmdb_data(movie_id)

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    query = args.get("query")
    print(query, file=sys.stderr)
    return controller.search_movie(query)
 
@app.route('/genres', methods=['GET'])
def get_genres():
    return controller.get_genre_type()

# did people who tend to give high/low ratings give this film a
# high/low rating too
@app.route('/q3_1_reaction', methods=['GET'])
def get_reaction():
    args = request.args
    movieId = args.get("movie_id")
    group = args.get("group") # Type "high" for High Raters, "low" for Low Raters
    return controller.get_reaction(movieId, group)


@app.route('/q3_2_reaction_genre', methods=['GET'])
def get_reaction_genre():
    args = request.args
    movieId = args.get("movie_id")
    group = args.get("group") # Type "high" for High Raters, "low" for Low Raters
    return controller.get_reaction_genre(movieId, group)

# Get the average rating for movies with specified 'tag'
# Explore relationship between tag data and rating
# If tag is not in db, return empty list
@app.route('/q4_1_tag_rating', methods=['GET'])
def get_tag_rating():
    args = request.args
    tag = args.get("tag") 
    return controller.get_tags_rating(tag)

# Explore relationship between tag data and genres
# Display all the tags associated with a specified 
# 'genre' and how many there are in the genre
@app.route('/q4_2_wordcloud', methods=['GET'])
def get_genre_tags():
    args = request.args
    genre = args.get("genre") # all the tags associated with this genre
    return controller.get_genre_tags(genre)

# Get the list of genres for the heatmap
@app.route('/q4_heat_genre_list',methods=['GET'])
def genre_list():
    return controller.genre_list()

# Get the list of tags for the heatmap
# specify 'n_tags' to get as many tags as you need
@app.route('/q4_heat_tags_list',methods=['GET'])
def tags_list():
    args = request.args
    n_tags = args.get("n_tags")
    return controller.tags_list(n_tags)

# Get the percentage of movies in the specified 'genre'
# that share the specified 'tag' (for the heatmap)
@app.route('/q4_heat_perc_w_tag',methods=['GET'])
def perc_w_tag():
    args = request.args
    genre = args.get("genre")
    tag = args.get("tag")
    return controller.perc_w_tag(genre,tag)

# Get the 25 most occurring tags for the genre
# and the data for the heatmap
@app.route('/q4_heatmap',methods=['GET'])
def tags_occur():
    args = request.args
    genre = args.get("genre")
    return controller.most_occurring_tags(genre)



# Q6.2: Personnality radar plot of the average person that likes, dislikes a genre
@app.route('/q6',methods=['GET'])
def personality():
    args = request.args
    low_high = args.get("type")
    genre = args.get("genre")
    return controller.genre_personality_avg(low_high,genre)
@app.route('/q62',methods=['GET'])
def personality2():
    return controller.Fav_genre_per_personality()

@app.route('/q6_1_avg_rating_personality', methods=['GET'])
def avg_rating_personality():
    args = request.args
    movieId = args.get("movie_id")
    group = args.get("group") # Type "high" for High Raters, "low" for Low Raters
    return controller.get_avg_rating_for_all_personality(movieId, group)

@app.after_request
def after_request(response):
   response.headers.add('Access-Control-Allow-Origin', '*')
   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
   return response

if __name__ == "__main__":
    app.debug = True
    app.run(host ='0.0.0.0', port=5000)
