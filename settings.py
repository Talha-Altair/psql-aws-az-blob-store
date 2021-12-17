import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES = {
    'user'      : os.environ['POSTGRES_USER'],
    'password'  : os.environ['POSTGRES_PASSWORD'],
    'database'  : os.environ['POSTGRES_DB'],
    'host'      : os.environ['POSTGRES_HOST'],
    'port'      : os.environ['POSTGRES_PORT'],
}

AZ_STORAGE_CONNECTION_STRING = os.environ['AZ_STORAGE_CONNECTION_STRING']

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']