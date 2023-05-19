# Capstone project

## ADF Dataflow Creation: 
Start by creating an ADF dataflow, which is a visual representation of data transformation logic. In this case, we've used two notebooks for data preprocessing and model building.

## Data Preprocessing Notebook
The data preprocessing notebook contains the code that performs the necessary transformations on our raw data. This can include tasks like data cleaning, feature engineering, data enrichment, or any other data preparation steps required before feeding it into the model building process.

## Model Building Notebook
The model building notebook contains the code for training your machine learning model. This notebook uses the preprocessed data as input and performs the necessary steps to build and train the model, such as selecting algorithms, tuning hyperparameters, and evaluating the model's performance.

## Dataflow creation
![Dataflow Image](https://github.com/sarangunasekara/azure-assignment/assets/96530239/4d293a7d-3bb7-40d8-9b3f-51792d730017)
Once you have the dataflow and notebooks ready, create an ADF dataflow. This is a helper thing that would give insight on relationship between smoking habits and diabetes. This will save into a csv file in a container.

## ADF Pipeline Creation
![Pipeline Image](https://github.com/sarangunasekara/azure-assignment/assets/96530239/77a73d1a-396a-4dd9-bd28-eef534c0f864)
A pipeline is a logical grouping of activities that define the workflow and dependencies between different components. In this case, your pipeline will consist of two activities: the data preprocessing activity and the model building activity.

## Data Preprocessing Activity: 
In your ADF pipeline, configure the data preprocessing activity to use the dataflow you created earlier. This activity triggers the execution of the dataflow and applies the transformations defined in the preprocessing notebook to your input data.

## Model Building Activity: 
Configure the model building activity in the pipeline to execute the model building notebook. This activity takes the preprocessed data from the previous step and performs the necessary steps to train and build the machine learning model.

## Manual Triggering
![pipeline activity runs](https://github.com/sarangunasekara/azure-assignment/assets/96530239/64077e82-413a-4f7b-baad-ac81b18c6362)
With your ADF pipeline configured, you can manually trigger its execution. This allows you to control when the data preprocessing and model building activities run. Manual triggering is useful when you want to test or validate the pipeline's functionality before scheduling it for automatic execution.

## Pipeline Run Validation 
Once the pipeline run is triggered, monitor its execution and validate its outcome. Check the logs, execution details, and any generated output or artifacts to ensure that the data preprocessing and model building activities completed successfully. You can also inspect the intermediate data produced during the dataflow and model building process to verify the transformations and model training.

