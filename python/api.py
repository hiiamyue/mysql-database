# import mysql.connector
from flask import Flask
from controller import Controller

controller =Controller()

app = Flask(__name__)

@app.route('/')
def default_data():
    #return controller.get_default_data()
    return controller.get_film_by_gern()

# @app.route('/sort_date')
# def sort_date():
#     return controller.sort_by_date()

# @app.route('/sort_title')
# def sort_title():
#     return controller.sort_by_title()

# @app.route('/sort_rating')
# def sort_rating():
#     return controller.sort_by_rating()

if __name__ == "__main__":
    app.run(host ='0.0.0.0')
