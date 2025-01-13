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
7. 
