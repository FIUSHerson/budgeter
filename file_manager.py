import os
import errno

def create_dir(path, access_rights):
    if not os.path.exists(path):
        try:
            os.makedirs(path, access_rights)
            print("Created path at " + path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    else:
        print("Directory at " + path + " already exists!")

def create_db_file(path, access_rights):
    if not os.path.exists(path):
        try:
            os.mknod(path)
            print("Created file at " + path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    else:
        print("File at " + path + " already exists!")