import os

STORAGE_PATH = os.getenv('STORAGE_PATH', '')
DEBUG = bool(os.environ.get('DEBUG', 'False').lower() in ("true", "yes", "t", "1"))
