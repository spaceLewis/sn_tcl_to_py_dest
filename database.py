

package database

import tclodbc
import logging

DB_Open = False
logger = logging.getLogger(__name__)

def connect():
    global DB_Open
    if not DB_Open:
        try:
            tclodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=mydatabase;UID=myusername;PWD=mypassword')
            DB_Open = True
            logger.info('Database connection established')
        except Exception as e:
            logger.error(f'Failed to establish database connection: {e}')

def execute_query(query):
    if DB_Open:
        try:
            cursor = tclodbc.cursor()
            if not query:
                logger.error('Query is empty')
                return []
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            logger.error(f'Failed to execute query: {e}')
            return []
    else:
        logger.error('Database is not open')
        raise Exception('Database is not open')