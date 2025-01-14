###
# This file connects to an Azure storage account using an Azure key vault secret
# in order to upload a local dataset file, and to serve as an example for future
# storage account operations. Requires the user to be logged into an Azure account
# or a managed identity to have the sufficient authorization in order to use
# DefaultCredential.
# Alternatively could use environment variables for secret-keeping
###

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

key_vault_name = "badgeprojectkv"
secret_name = "badgeprojectsa-constring"
storage_account_name = "badgeprojectsa"

key_vault_url = f"https://{key_vault_name}.vault.azure.net/"

# Create a DefaultAzureCredential object
credential = DefaultAzureCredential()

# Create a SecretClient object
secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

# Retrieve the secret value
secret = secret_client.get_secret(secret_name)
connection_string = secret.value

container_name = "raw"

local_file_path = "./marketing_campaign.csv"

# Create a BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Create a ContainerClient object
container_client = blob_service_client.get_container_client(container_name)

# Create the container if it does not exist
try:
    container_client.create_container()
except Exception as e:
    print(f"Container already exists: {e}")

# Create a BlobClient object
# target file name
blob_name = "client_data.csv"
blob_client = container_client.get_blob_client(blob_name)

# Upload the local file to the blob
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data)

print(f"File {local_file_path} uploaded to blob {blob_name} in container {container_name}.")