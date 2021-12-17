import psycopg2
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import settings

db_connection = psycopg2.connect(**settings.POSTGRES)

az_storage_string = settings.AZURE_STORAGE_CONNECTION_STRING

blob_service_client = BlobServiceClient.from_connection_string(az_storage_string)