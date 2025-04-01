

import os
import git
import tclodbc
import configparser

# Initialize environment variables
os.environ['COMPUTERNAME'] = 'localhost'

# Set up database connection
try:
    db_connection = tclodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=mydatabase;UID=myusername;PWD=mypassword')
except tclodbc.Error as e:
    print(f"Error connecting to database: {e}")
    exit(1)

# Load libraries and procedures
from config_reader import ReadConfigValues

# Check current Git branch and commit status
try:
    repo = git.Repo(search_parent_directories=True)
    current_branch = repo.active_branch
    commit_status = repo.git.status()
    if current_branch.name != 'main':
        print("Error: Not on main branch")
        exit(1)
    if commit_status != '':
        print("Error: Uncommitted changes")
        exit(1)
except git.exc.GitError as e:
    print(f"Error checking Git status: {e}")
    exit(1)

# Set variables
globAbbruchFlag = False
theTestDirList = []
theTestDir = ''
theTestFileList = []
theTestProcList = []
theDevList = []

# Read configuration values from ini-file
config = configparser.ConfigParser()
try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Error reading config file: {e}")
    exit(1)

# Check required configuration values
required_values = ['test_dir', 'test_file', 'test_proc', 'dev_list']
for value in required_values:
    if not config.has_option('DEFAULT', value):
        print(f"Error: Missing required configuration value '{value}'")
        exit(1)

# Set variables based on configuration values
theTestDirList = config.get('DEFAULT', 'test_dir').split(',')
theTestDir = theTestDirList[0]
theTestFileList = config.get('DEFAULT', 'test_file').split(',')
theTestProcList = config.get('DEFAULT', 'test_proc').split(',')
theDevList = config.get('DEFAULT', 'dev_list').split(',')

# Call ReadConfigValues procedure
try:
    ReadConfigValues(config)
except Exception as e:
    print(f"Error calling ReadConfigValues: {e}")
    exit(1)