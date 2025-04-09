

import mysql.connector
from mysql.connector import Error

def connect_to_database(host, database, user, password):
    if not all([host, database, user, password]):
        raise ValueError("All connection parameters must be provided")
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        return connection
    except Error as err:
        raise ConnectionError("Failed to connect to database: {}".format(err))

def execute_query(connection, query):
    if not connection or not query:
        raise ValueError("Connection and query must be provided")
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        raise RuntimeError("Failed to execute query: {}".format(err))

def close_connection(connection):
    if not connection:
        raise ValueError("Connection must be provided")
    try:
        connection.close()
    except Error as err:
        raise RuntimeError("Failed to close connection: {}".format(err))