

import sqlite3
import logging

# Set up logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

# Set up database connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def lw(message):
    logging.info(message)

def SQL_DeleteOldLog(days):
    try:
        cursor.execute('DELETE FROM log WHERE timestamp < datetime("now", "-{} days")'.format(days))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_DeleteOldLog: {}".format(e))

def SQL_DeleteAllOldLog():
    try:
        cursor.execute('DELETE FROM log')
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_DeleteAllOldLog: {}".format(e))

def SQL_DeleteLog(log_id):
    try:
        cursor.execute('DELETE FROM log WHERE id = ?', (log_id,))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_DeleteLog: {}".format(e))

def SQL_DeleteTcIdLines(tc_id):
    try:
        cursor.execute('DELETE FROM log WHERE tc_id = ?', (tc_id,))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_DeleteTcIdLines: {}".format(e))

def SQL_DeleteTestRunLine(test_run_id):
    try:
        cursor.execute('DELETE FROM test_run WHERE id = ?', (test_run_id,))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_DeleteTestRunLine: {}".format(e))

def SQL_DeleteLogErrTable():
    try:
        cursor.execute('DELETE FROM log_err')
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_DeleteLogErrTable: {}".format(e))

def SQL_DeleteLogTable():
    try:
        cursor.execute('DELETE FROM log')
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_DeleteLogTable: {}".format(e))

def SQL_WriteLog(log_entry):
    try:
        cursor.execute('INSERT INTO log (timestamp, message) VALUES (?, ?)', (log_entry['timestamp'], log_entry['message']))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_WriteLog: {}".format(e))

def SQL_WriteLogErr(log_err_entry):
    try:
        cursor.execute('INSERT INTO log_err (timestamp, message) VALUES (?, ?)', (log_err_entry['timestamp'], log_err_entry['message']))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_WriteLogErr: {}".format(e))

def SQL_WriteLogTC(log_tc_entry):
    try:
        cursor.execute('INSERT INTO log_tc (timestamp, message) VALUES (?, ?)', (log_tc_entry['timestamp'], log_tc_entry['message']))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_WriteLogTC: {}".format(e))

def SQL_NewDefaultTestRun():
    try:
        cursor.execute('INSERT INTO test_run (description) VALUES ("Default Test Run")')
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_NewDefaultTestRun: {}".format(e))

def SQL_WriteTestRun(test_run_entry):
    try:
        cursor.execute('INSERT INTO test_run (description) VALUES (?)', (test_run_entry['description'],))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_WriteTestRun: {}".format(e))

def SQL_UpdateTestRun(test_run_id, description):
    try:
        cursor.execute('UPDATE test_run SET description = ? WHERE id = ?', (description, test_run_id))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_UpdateTestRun: {}".format(e))

def SQL_UpdateTestRun_DescriptionPrefix(test_run_id, prefix):
    try:
        cursor.execute('UPDATE test_run SET description = ? || description WHERE id = ?', (prefix, test_run_id))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQL_UpdateTestRun_DescriptionPrefix: {}".format(e))

def db(query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        logging.error("db: {}".format(e))

def TlPrint(message):
    print(message)

def TlInput(prompt):
    return input(prompt)