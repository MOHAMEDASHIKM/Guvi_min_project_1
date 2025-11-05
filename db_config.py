import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",            # your MySQL username
        password="Ashik@123",# your MySQL password
        database="client_query_db"
    )
    return conn
