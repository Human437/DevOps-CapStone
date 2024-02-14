from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
import uuid
import qrcode
from io import BytesIO

# Loading Environment variable
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Allowing CORS for local testing
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Azure Configuration
storage_account_name = "devopsqrcodegenerator"
container_name = "qr-codes"


@app.post("/generate-qr-code/")
async def generate_qr_code(url: str):
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR Code to BytesIO object
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Local QR Code testing
    try:
        # QR codes naming
        local_directory = f'./{container_name}'
        local_file_name = str(uuid.uuid4()) + ".png"
        local_file_path = local_directory + "/" + local_file_name

        # Check if local directory exists; if not create it
        # if not os.path.isdir(local_directory):
        #     os.mkdir(local_directory)

        # Write QR Code locally
        # img.save(local_file_path)

    except Exception as ex:
        print('Failed to do stuff locally - Exception:')
        print(
            f"An exception of type {type(ex).__name__} occurred. Arguments:\n{ex.args[0]}")

    # Authenticate with Azure
    try:
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

        # Create the BlobServiceClient object using a connection string
        blob_service_client = BlobServiceClient.from_connection_string(
            connect_str)
    except ValueError:
        # Azure Connection String not defined, attempt to use managed identity
        account_url = f"https://{storage_account_name}.blob.core.windows.net"
        default_credential = DefaultAzureCredential()

        # Create the BlobServiceClient object using a managed identity
        blob_service_client = BlobServiceClient(
            account_url, credential=default_credential)
    except Exception as ex:
        print('Failed to connect to Azure - Exception:')
        print(
            f"An exception of type {type(ex).__name__} occurred. Arguments:\n{ex.args[0]}")

    # Write QR Code to Azure
    try:
        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(
            container=container_name, blob=local_file_name)

        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

        # Upload the QR Code
        blob_client.upload_blob(img_byte_arr)

        # Generate Azure Blob URL
        azure_blob_url = f'https://{storage_account_name}.blob.core.windows.net/{container_name}/{local_file_name}'
        return {"qr_code_url": azure_blob_url}

    except Exception as ex:
        print('Failed to write QR code to Azure - Exception:')
        print(
            f"An exception of type {type(ex).__name__} occurred. Arguments:\n{ex.args[0]}")
