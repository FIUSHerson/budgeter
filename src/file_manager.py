import os, errno
from terminal_formatter import print_crit, print_warn, print_norm

def create_dir(path, access_rights):
    if not os.path.exists(path):
        try:
            os.makedirs(path, access_rights)
            print_norm("Created path at " + path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    else:
        print_warn("Directory at " + path + " already exists!")

def create_db_file(path, access_rights):
    if not os.path.exists(path):
        try:
            os.mknod(path)
            print_norm("Created file at " + path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    else:
        print_warn("File at " + path + " already exists!")