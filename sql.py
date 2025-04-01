

import sqlite3
import logging
from datetime import datetime, timedelta

class SQL:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.logger = logging.getLogger(__name__)

    def SQL_DeleteOldLog(self, days):
        try:
            days = int(days)
            if days < 0:
                self.logger.error("Invalid input for days")
                return
            date = datetime.now() - timedelta(days=days)
            self.cursor.execute("DELETE FROM log WHERE date < ?", (date.strftime("%Y-%m-%d"),))
            self.conn.commit()
            self.logger.info(f"Deleted old log files older than {days} days")
        except sqlite3.Error as e:
            self.logger.error(f"Error deleting old log files: {e}")
        except Exception as e:
            self.logger.error(f"Error deleting old log files: {e}")

    def SQL_NewDefaultTestRun(self, test_name):
        try:
            if not test_name:
                self.logger.error("Invalid input for test_name")
                return
            self.cursor.execute("INSERT INTO test_runs (test_name, status) VALUES (?, 'running')", (test_name,))
            self.conn.commit()
            self.logger.info(f"Created new default test run for {test_name}")
        except sqlite3.Error as e:
            self.logger.error(f"Error creating new default test run: {e}")
        except Exception as e:
            self.logger.error(f"Error creating new default test run: {e}")

    def close(self):
        self.conn.close()