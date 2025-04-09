

import os
import configparser
import git
from utils import Utils
from database import Database

# Define environment variables
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')
INI_FILE = os.environ.get('INI_FILE', 'config.ini')

# Load configuration values from INI file
config = configparser.ConfigParser()
config.read(INI_FILE)

# Set up paths for test environment
MAIN_PATH = config.get('paths', 'main_path')
LIBRARY_PATH = config.get('paths', 'library_path')
INITIALIZATION_PATH = config.get('paths', 'initialization_path')
OBJEKT_DB_PATH = config.get('paths', 'objekt_db_path')

# Set up database connections
DB_HOST = config.get('database', 'host')
DB_USER = config.get('database', 'user')
DB_PASSWORD = config.get('database', 'password')
DB_NAME = config.get('database', 'name')

try:
    # Check current Git branch and commit status
    repo = git.Repo()
    current_branch = repo.active_branch
    commit_status = repo.git.status()

    # Validate current Git branch and commit status
    if current_branch != 'main':
        raise ValueError("Invalid Git branch")
    if commit_status != '':
        raise ValueError("Uncommitted changes detected")

    # Initialize database connection
    db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_PASSWORD, DB_NAME)
    db.connect()

    # Load libraries
    utils = Utils()
    database = Database()

except Exception as e:
    print(f"Error: {e}")
    exit(1)