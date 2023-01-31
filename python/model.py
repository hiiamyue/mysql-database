# import mysql.connector

# print('reached')
# connection = mysql.connector.connect(
#     user='root', password='sushiroll', host='mysql', port='3306', database='db')
# print('DB connected')


# cursor = connection.cursor()
# cursor.execute('SELECT * FROM movies')
# movies = cursor.fetchall()
# connection.close()

# print(movies)

import mysql.connector
import json
from flask import Flask

print('reached')
connection = mysql.connector.connect(
   user='root', password='sushiroll', host='mysql', port='3306', database='db')
print('DB connected')

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
