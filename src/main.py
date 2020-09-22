import sqlite3
from sqlite3 import Error
from file_manager import *

print("Starting budgeter...")

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def init():
    # Define some variables
    folder_path = os.environ['HOME'] + "/.config/budgeter-dev"
    file_path = folder_path + "/budgeter-config.db"
    access_rights = 0o755

    # Create neccessary files
    print("Creating files if they don't exist...")
    create_dir(folder_path, access_rights)
    create_db_file(file_path, access_rights)

    # Connect to database
    create_connection(file_path)

if __name__ == "__main__":
    init()