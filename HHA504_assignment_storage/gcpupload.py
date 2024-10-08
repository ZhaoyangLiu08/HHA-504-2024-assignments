from google.cloud import storage

bucket_name = "storage-testkliu-gcp"
destination_blob_name = "IM-0001-0001.jpeg"
source_file_name = "D:\HHA\IM-0001-0001.jpeg"

storage_client = storage.Client()

bucket = storage_client.get_bucket(bucket_name)

blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

print(f"{source_file_name} has been uploaded to GCP Cloud Storage as {destination_blob_name}.")
