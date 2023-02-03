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
        self.cursor = self.db.cursor()

    def get_default_data(self):
        self.cursor.execute("SELECT * FROM movies")
        movies = self.cursor.fetchall()
        self.cursor.close()
        return movies

    def sort_by_date(self):
        self.cursor.execute("SELECT * FROM movies \n ORDER BY release_date")
        movies = self.cursor.fetchall()
        self.cursor.close()
        return movies
    
    def sort_by_title(self):
        self.cursor.execute("SELECT * FROM movies \n ORDER BY title")
        movies = self.cursor.fetchall()
        self.cursor.close()
        return movies