# Flask App for Listing Files in Azure Blob Storage
This Flask app allows you to list filenames present in specific folders of an Azure Blob Storage container. The app is deployed on a virtual machine (VM) in the East US region and can only be accessed from the Tiger VPN. Follow the instructions below to set up the environment and deploy the app.

### Prerequisites
- Azure subscription
- Azure CLI installed on your local machine
- Tiger VPN access

## Step 1: Resource Group Creation
Already, the resource group has been created in the East US region.

## Step 2: Storage Account Creation
Create a storage account in the "cloud_training" resource group and the East US region in the portal or using Azure CLI command.

## Step 3: Container and Folders Creation
Create a container and three folders ("sample1", "sample2", "sample3") inside the container and upload random files inside each folder. This will display in our Flask web application that we about to create in subsequent steps.

### Step 4: Flask App Deployment
Copy the Flask app code provided in the question to a file named app.py on your local machine.

```sh
from flask import Flask, redirect, url_for, request, render_template, jsonify
from azure.storage.blob import ContainerClient, BlobClient
import os

app = Flask(__name__)

# Get request
@app.route('/<foldername>')
def list_all_dirs(foldername):
    res = []
    connect_str = 'XXXXXX-XXX-XXXXXXX'  # Replace with your actual connection string
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
```

## Step 5: Virtual Network Creation
Create a virtual network (VNET) with a subnet in the East US region.

## Step 6: VM Creation
Create a VM in the "cloud_training" resource group, within the VNET and subnet created above, with a Standard_A2_v2 size, a public IP, and a 10GB disk. 

## Step 7: Flask App Deployment to VM
Copy the app.py file containing the Flask app code to the VM. And run by using ```python3 app.py run```

# Overview about code
 - The provided code is a Flask application that interacts with Azure Blob Storage to list filenames in specific folders within a container. Let's go over the code and understand its functionality:

- The code starts by importing necessary modules, including Flask and Azure Blob Storage-related modules.

- An instance of the Flask application is created with app = ```Flask(__name__).```

- The main route of the application is defined using the @app.route decorator. The route accepts a ```<foldername>``` parameter in the URL.

- Within the route function fun(foldername), the code establishes a connection to Azure Blob Storage using the provided storage account connection string. It creates a ContainerClient object to work with a specific container named "cont".

- It then retrieves a list of blobs (files) within the container using ```blob_service_client.list_blobs()```.

- The code iterates over each blob and checks if its folder name matches the provided ```<foldername>```. If it does, the corresponding filename is extracted and added to the res list.

- Finally, the res list is returned as a JSON response using jsonify(res).

- The if ```__name__ == '__main__'```: block ensures that the Flask application is only run when the script is executed directly (not when imported as a module). It starts the Flask development server on ```0.0.0.0:5000.```

- Overall, this code sets up a Flask API that listens for requests with a folder name parameter in the URL. It establishes a connection to Azure Blob Storage, retrieves a list of filenames within the specified folder, and returns them as a JSON response.

