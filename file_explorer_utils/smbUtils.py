import hashlib


def calculate_md5(smbClient, path):
    return hashlib.md5(smbClient.open(path, 'rb').read()).hexdigest()
