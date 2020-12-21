import os
import hashlib


def join(path, name):
    return os.path.join(path, name)


def calculate_md5(path):
    return hashlib.md5(open(path,'rb').read()).hexdigest()


def get_size(path):
    return os.path.getsize(path)
