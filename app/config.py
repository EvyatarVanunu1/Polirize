import os
import pathlib


SECRET = 'top_secret'
JWT_HASH_ALGO = 'HS256'
PASSWORD_FILE = os.path.join(pathlib.Path(__file__).parent.absolute(), 'password_file.json')
