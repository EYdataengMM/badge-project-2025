# badge-project-2025

# Goals:
1. Create a showcase app connecting Data Engineering and ML-related tools and Azure services
2. Create a useful POC prediction app
3. Explore

# The overall picture:
1. Use data about customer profiles and buying preferences to create a model able to predict whether a product should be advertised to them
2. Allow for online testing hypothetis of advertising to specific clients
3. Utilize modern MLOps tools like:  
  - AzureML
  - MLFlow
  -  GitHub Actions
  - Airflow

# Steps to take:
1. Find a suitable dataset - DONE - https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis
2. Upload the dataset to a storage account, set up code connection to Azure services
3. Train the model using sklearn and mlflow
4. Optimize training using GitHub Actions, Optuna and other tools AKA set up a pipeline of downloading the data, cleanup and training
5. Orchestrate everything and set up in AzureML for model access?
6. Create a web app with model endpoint access for testing new client data

## Even more specific steps:
1. To demonstrate orchestration, use databricks and pyspark to prepare the data
2. Then use AzureML to read in the data and run mlflow and optuna based training
3. Airflow? To run the download of the dataset from kaggle, then to start an AzureML pipeline? And then download the best model to a storage account and use it to update the model used in the webapp deployment?
4. GitHub Actions? How?

## Therefore:
1. Connect databricks workspace to storage account and AzureML workspace
2. Clean-up the data in databricks then upload to AzureML datasets from within Databricks
3. Create a pipeline in AzureML to run the Databricks Step (clean up and upload to AzureML datastore)
4. Create steps in AzureML pipeline to use the AzureML dataset and mlflow to train the model and save in model repository
5. Create a web app to use the model
6. Create a local script with Airflow to run the AzureML pipeline and run the script creating the web app using the most recent trained model from AzureML - is this necessary?
7. Is using Airflow Docker and environmental variables for Azure secrets will also be necessary
8. 
