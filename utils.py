

import configparser
import git
import mysql.connector
import time
import threading

def print_message(message):
    print(message)

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        print("Invalid input. Please try again.")

def read_config_values(file_path, section, key):
    try:
        config = configparser.ConfigParser()
        config.read(file_path)
        return config.get(section, key)
    except configparser.Error as e:
        print(f"Error reading configuration file: {e}")
        return None

def check_git_branch_and_commit(repo_path):
    try:
        repo = git.Repo(repo_path)
        branch = repo.active_branch
        commit = repo.head.commit
        return branch.name, commit.hexsha
    except git.exc.GitError as e:
        print(f"Error checking Git status: {e}")
        return None, None

def connect_to_database(host, user, password, database):
    try:
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def doWaitForObject(obj, timeout):
    start_time = time.time()
    while obj is None:
        if time.time() - start_time > timeout:
            raise TimeoutError("Object not set within timeout")
        time.sleep(0.1)

def doWaitMs(ms):
    time.sleep(ms / 1000)

def checkAllRelayStatus(device):
    if hasattr(device, 'check_relay_status'):
        return device.check_relay_status()
    else:
        print("Device object does not have a check_relay_status method")
        return None