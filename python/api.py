import mysql.connector
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():

    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="sushiroll",
        database="db"
    )
    cursor = mydb.cursor()


    cursor.execute("SELECT title FROM movies")
    movies = cursor.fetchall()
    mydb.close()

    return movies


if __name__ == "__main__":
    app.run(host ='0.0.0.0')
