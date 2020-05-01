import os


def get_api_token(key='API_TOKEN'):
    """Simple retrieval function.
    Returns API_TOKEN or raises OSError."""
    api_token = os.getenv(key, default=None)

    if api_token is None:
        raise OSError("API_TOKEN environment is not set.")

    return api_token
