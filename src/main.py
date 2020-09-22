import sqlite3, argparse, os
from sqlite3 import Error
from file_manager import create_dir, create_db_file
from terminal_formatter import print_crit, print_warn, print_norm
from db_init import db_setup

print_norm("")
print_norm("Starting budgeter...")
print_norm("")

def create_connection(db_file):
    # Create a database connection to a SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print_norm("Connected using sqlite3 v" + sqlite3.version)
    except Error as e:
        print_crit(e)
    finally:
        if conn:
            conn.close()

def init():
    # Define some variables
    folder_path = os.environ['HOME'] + "/.config/budgeter-dev"
    file_path = folder_path + "/budgeter-config.db"
    access_rights = 0o755

    # Create neccessary files
    print_norm("Creating files if they don't exist...")
    create_dir(folder_path, access_rights)
    create_db_file(file_path, access_rights)

    # Connect to database
    create_connection(file_path)

def parse_args():
    parser = argparse.ArgumentParser(description = "Allows some command-line arguments")
    subparsers = parser.add_subparsers()

    parser_init = subparsers.add_parser('init')
    parser_init.set_defaults(func=db_setup)

    args = parser.parse_args('init'.split())
    args.func()

if __name__ == "__main__":
    init()
    parse_args()