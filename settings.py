import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES = {
    'username'  : os.environ['POSTGRES_USER'],
    'password'  : os.environ['POSTGRES_PASSWORD'],
    'database'  : os.environ['POSTGRES_DB'],
    'host'      : os.environ['POSTGRES_HOST'],
    'port'      : os.environ['POSTGRES_PORT'],
}

