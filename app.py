import pandas as pd
from connections import db_connection, blob_service_client, s3_client

def upload_to_az_container(local_file_path, container_name, blob_name) -> int:
    """
    Uploads to azure blob container with blob name
    """

    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(blob_name)

    with open(local_file_path, "rb") as data:

        blob_client.upload_blob(data, overwrite=True)

    return 0

def download_az_blob(container_name, blob_name, download_file_path) -> int:
    """
    Downloads blob from azure blob container to local file
    """

    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(blob_name)

    with open(download_file_path, "wb") as download_file:

        download_file.write(blob_client.download_blob().readall())

    return 0

def download_file_from_s3(bucket_name, file_name, download_file_path) -> int:
    """
    Downloads file from s3 bucket
    """

    s3_client.download_file(bucket_name, file_name, download_file_path)

    return 0

def upload_file_to_s3(local_file_path, bucket_name, file_name) -> int:
    """
    Uploads file to s3 bucket
    """

    s3_client.upload_file(local_file_path, bucket_name, file_name)

    return 0

def read_table_from_psql(table_name) -> pd.DataFrame:
    """
    Reads table from psql
    """

    df = pd.read_sql_query(f"SELECT * FROM {table_name}", db_connection)

    return df

if __name__ == "__main__":
    
    df = read_table_from_psql("links")

    df.to_csv("data/links.csv", index = False)
    
    # upload_to_az_container("data/links.csv", "talha", "one/links.csv")

    # download_az_blob("talha", "one/links.csv", "data/links_downloaded.csv")

    upload_file_to_s3("data/links.csv", "talhaaltair", "two/links.csv")

    download_file_from_s3("talhaaltair", "two/links.csv", "data/links_downloaded_2.csv")
          