import os


def get_token(key='API_TOKEN'):
    return os.getenv(key, default=None)
