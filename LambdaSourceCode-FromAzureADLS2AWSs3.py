import os
import boto3
import requests
from io import BytesIO
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient, ContainerClient
from azure.core.exceptions import ResourceNotFoundError
def download_blob_with_sdk():
    try:
        account_url = f"https://{os.environ['AZURE_STORAGE_ACCOUNT']}.blob.core.windows.net"
        container_name = os.environ['AZURE_CONTAINER_NAME']
        blob_name = "mock_data_io.xlsx"
        # Explicitly use Service Principal authentication
        credential = ClientSecretCredential(
            tenant_id=os.environ['AZURE_TENANT_ID'],
            client_id=os.environ['AZURE_CLIENT_ID'],
            client_secret=os.environ['AZURE_CLIENT_SECRET']
        )
        blob_service_client = BlobServiceClient(account_url, credential=credential)
        blob_client = blob_service_client.get_blob_client(container_name, blob_name)
        try:
            return blob_client.download_blob().readall()
        except ResourceNotFoundError:
            print(f"Blob {blob_name} not found in container {container_name}")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
def lambda_handler(event, context):
    try:
        file_name = "mock_data_io.xlsx"
        print(f"Processing file: {file_name}")
        
        file_content = download_blob_with_sdk()
        
        if not file_content:
            raise Exception(f"Failed to download {file_name} from Azure Blob Storage.")
        
        s3_client = boto3.client('s3')
        s3_client.upload_fileobj(
            BytesIO(file_content),
            os.environ['S3_BUCKET'],
            file_name
        )
        
        return {
            'statusCode': 200,
            'body': f'Successfully transferred {file_name} to S3'
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': str(e)
        }