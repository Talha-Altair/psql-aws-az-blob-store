import pandas as pd
from connections import db_connection, blob_service_client

def upload_to_az_container(local_file_path, container_name, blob_name):
    """
    Uploads to azure blob container with blob name
    """

    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(blob_name)

    with open(local_file_path, "rb") as data:

        blob_client.upload_blob(data, overwrite=True)

    return 0

def download_az_blob(container_name, blob_name, download_file_path):
    """
    Downloads blob from azure blob container to local file
    """

    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(blob_name)

    with open(download_file_path, "wb") as download_file:

        download_file.write(blob_client.download_blob().readall())

    return 0

def read_table_from_psql(table_name):
    """
    Reads table from psql
    """

    df = pd.read_sql_query(f"SELECT * FROM {table_name}", db_connection)

    return df

if __name__ == "__main__":
    
    df = read_table_from_psql("links")

    df.to_csv("data/links.csv", index = False)
    
    upload_to_az_container("data/links.csv", "talha", "one/links.csv")

    download_az_blob("talha", "one/links.csv", "data/links_downloaded.csv")
          