import mysql.connector

print('reached')
connection = mysql.connector.connect(
    user='root', password='sushiroll', host='mysql', port='3306', database='db')
print('DB connected')


cursor = connection.cursor()
cursor.execute('SELECT * FROM movies')
movies = cursor.fetchall()
connection.close()

print(movies)