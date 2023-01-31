import mysql.connector

class Model:
    def __init__(self) -> None:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            password="sushiroll",
            database="db"
        )
        self.db = mydb

    def get_default_data(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM movies")
        movies = cursor.fetchall()
        return movies
