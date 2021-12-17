import pandas as pd
import psycopg2

import settings

connection = psycopg2.connect(**settings.POSTGRES)

import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

connect_str = 12

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Create a unique name for the container
container_name = str(uuid.uuid4())

# Create the container
container_client = blob_service_client.create_container(container_name)

local_file_name = "downloaded_file.csv"

blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

download_file_path = "downloaded_file.csv"

with open(download_file_path, "wb") as download_file:

    download_file.write(blob_client.download_blob().readall())

# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

upload_file_path = "uploaded_file.csv"

# Upload the created file
with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)              