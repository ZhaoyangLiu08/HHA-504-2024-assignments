import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = "containers-test"
blob_name = "IM-0001-0001.jpeg"
local_file_path = "D:\HHA\IM-0001-0001.jpeg"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service_client.get_container_client(container_name)

blob_client = container_client.get_blob_client(blob_name)

with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data)

print(f"{local_file_path} has been uploaded to Azure Blob Storage as {blob_name}.")
