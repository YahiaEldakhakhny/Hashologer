# IMPORTS
import hashlib

# FUNCTION DEFINITIONS
def get_sha256(path):
    with open(path, 'rb') as opened_file:
        content = opened_file.read()
        sha256 = hashlib.sha256()
        sha256.update(content)
        return sha256.hexdigest()


