# import mysql.connector
from flask import Flask
from controller import Controller
from flask_cors import CORS


controller =Controller()

app = Flask(__name__)
# Add the CORS header to the json objects to avoid the error
CORS(app)

@app.route('/')
def default_data():
    #return controller.get_default_data()
    genre = ['Action']
    return controller.get_film_by_gern(genre)

# @app.route('/sort_date')
# def sort_date():
#     return controller.sort_by_date()

# @app.route('/sort_title')
# def sort_title():
#     return controller.sort_by_title()

# @app.route('/sort_rating')
# def sort_rating():
#     return controller.sort_by_rating()

#@app.after_request
#def after_request(response):
   # response.headers.add('Access-Control-Allow-Origin', '*')
   # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  #  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  #  return response

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=5000)
