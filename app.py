from flask import Flask, redirect, url_for, request, render_template, jsonify
from azure.storage.blob import ContainerClient, BlobClient
import os

app = Flask(__name__)

# Get request
@app.route('/<foldername>')
def list_all_dirs(foldername):
    res = []
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=gsaran;AccountKey=c0IAqwyo3s9k6XRB00TyPYb7D03aGaNjJwljKBN+Nzn8bYCvODAgCpmZyME/Aa1wBxSydsqoLCWE+ASt7uvP4A==;EndpointSuffix=core.windows.net'  # Replace with your actual connection string
    blob_service_client = ContainerClient.from_connection_string(connect_str, container_name="saran-input")
    blob_list = blob_service_client.list_blobs()

    for blob in blob_list:
        temp = str(blob.name)
        folder, file = temp.split('/')
        if folder == foldername:
            res.append(file)

    return render_template('files.html', foldername=foldername, files=res)



if __name__ == '__main__':
    app.run(app='app:app',host='0.0.0.0', debug=True)
