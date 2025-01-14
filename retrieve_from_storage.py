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

# Create a BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Create a ContainerClient object
container_client = blob_service_client.get_container_client(container_name)

# Create a BlobClient object
# target file name
blob_name = "client_data.csv"
blob_client = container_client.get_blob_client(blob_name)


### Grabbing the file

from io import BytesIO
import pandas as pd

# Download the blob content to a stream
blob_data = blob_client.download_blob()
blob_content = blob_data.readall()

# Read the CSV content into a pandas DataFrame
df = pd.read_csv(BytesIO(blob_content), sep='\t')

# Display a part of the DataFrame (e.g., first 5 rows)
print(df.head())