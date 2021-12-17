import psycopg2
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import settings
import boto3

db_connection = psycopg2.connect(**settings.POSTGRES)

az_storage_string = settings.AZ_STORAGE_CONNECTION_STRING

blob_service_client = BlobServiceClient.from_connection_string(az_storage_string)

s3_client = boto3.client('s3', 
                        aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
                    