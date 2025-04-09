

import sqlite3
from datetime import datetime, timedelta

class TestRunManagement:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def delete_old_log_tables(self):
        try:
            self.cursor.execute("DELETE FROM log_tables WHERE created_at < ?", (datetime.now() - timedelta(days=30),))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting old log tables: {e}")

    def write_log(self, log_message):
        try:
            self.cursor.execute("INSERT INTO logs (log_message, created_at) VALUES (?, ?)", (log_message, datetime.now()))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error writing log: {e}")

    def update_test_run_info(self, test_run_id, test_run_info):
        try:
            self.cursor.execute("UPDATE test_runs SET test_run_info = ? WHERE id = ?", (test_run_info, test_run_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating test run info: {e}")

    def delete_test_case_id_lines(self, test_case_id):
        try:
            self.cursor.execute("DELETE FROM test_case_id_lines WHERE test_case_id = ?", (test_case_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting test case id lines: {e}")

    def delete_test_run_lines(self, test_run_id):
        try:
            self.cursor.execute("DELETE FROM test_run_lines WHERE test_run_id = ?", (test_run_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting test run lines: {e}")

    def delete_error_entries(self, error_id):
        try:
            self.cursor.execute("DELETE FROM error_entries WHERE id = ?", (error_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting error entries: {e}")

    def delete_log_table_entries(self, log_table_id):
        try:
            self.cursor.execute("DELETE FROM log_table_entries WHERE log_table_id = ?", (log_table_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting log table entries: {e}")

    def write_log_entry(self, log_message):
        try:
            self.cursor.execute("INSERT INTO log_entries (log_message, created_at) VALUES (?, ?)", (log_message, datetime.now()))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error writing log entry: {e}")

    def write_error_log_entry(self, error_message):
        try:
            self.cursor.execute("INSERT INTO error_log_entries (error_message, created_at) VALUES (?, ?)", (error_message, datetime.now()))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error writing error log entry: {e}")

    def write_test_case_log_entry(self, test_case_id, log_message):
        try:
            self.cursor.execute("INSERT INTO test_case_log_entries (test_case_id, log_message, created_at) VALUES (?, ?, ?)", (test_case_id, log_message, datetime.now()))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error writing test case log entry: {e}")

    def create_default_test_run(self):
        try:
            self.cursor.execute("INSERT INTO test_runs (test_run_info, created_at) VALUES (?, ?)", ("Default Test Run", datetime.now()))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating default test run: {e}")

    def write_test_run(self, test_run_info):
        try:
            self.cursor.execute("INSERT INTO test_runs (test_run_info, created_at) VALUES (?, ?)", (test_run_info, datetime.now(), test_run_info))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error writing test run: {e}")

    def update_test_run(self, test_run_id, test_run_info):
        try:
            self.cursor.execute("UPDATE test_runs SET test_run_info = ? WHERE id = ?", (test_run_info, test_run_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating test run: {e}")

    def update_test_run_description_with_prefix(self, test_run_id, prefix):
        try:
            test_run_info = self.get_test_run_info(test_run_id)
            if test_run_info:
                self.cursor.execute("UPDATE test_runs SET test_run_info = ? WHERE id = ?", (prefix + " " + test_run_info, test_run_id))
                self.conn.commit()
            else:
                print("Test run ID not found")
        except sqlite3.Error as e:
            print(f"Error updating test run description with prefix: {e}")

    def get_test_run_info(self, test_run_id):
        try:
            self.cursor.execute("SELECT test_run_info FROM test_runs WHERE id = ?", (test_run_id,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error getting test run info: {e}")