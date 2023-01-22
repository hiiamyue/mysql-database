import mysql.connector
from  mysql.connector import Error

def connect():
    conn = None
    try :
        conn = mysql.connector.connect(
            host ='localhost',
            database ='mysql',
            user ='yue',
            password ='password')
        if conn.is_connected():
            print('connected to MySQL database')
    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ =='__main__':
    connect()
