# import mysql.connector
from flask import Flask
from controller import Controller

controller =Controller()

app = Flask(__name__)

@app.route('/')
def get_default_data():
    return controller.get_default_data()

# sort by date
# @app.route('/')
# def get_default_data():
#     return controller.sort_by_date()

# @app.route('/')
# def get_default_data():
#     return controller.sort_by_title()

if __name__ == "__main__":
    app.run(host ='0.0.0.0')
