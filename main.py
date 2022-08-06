# IMPORTS
import hashlib
from pathlib import Path

# FUNCTION DEFINITIONS
def get_sha256(path):
    with open(path, 'rb') as opened_file:
        content = opened_file.read()
        sha256 = hashlib.sha256()
        sha256.update(content)
        return sha256.hexdigest()


# Get file path from the user <Temporary until the GUI is ready>
curr_path = Path(input("Enter path of the target file: "))
print(get_sha256(curr_path))