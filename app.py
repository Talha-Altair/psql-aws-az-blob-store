import pandas as pd
import psycopg2

import settings

connection = psycopg2.connect(**settings.POSTGRES)