# End-to-End Machine Learning Project with MLOps and CI/CD

## Project Overview

This project is an end-to-end machine learning application that implements MLOps practices and CI/CD pipelines. It encompasses various phases, including data ingestion, transformation, model training, evaluation, and deployment using modern cloud technologies such as AWS and Azure. The primary focus of the project is to create a robust and scalable machine learning application that automates the entire workflow, enabling rapid development and deployment.

## Project Structure

The project is organized into several components:

- **Data Ingestion**: 
  - **File**: `data_ingestion.py`
  - This component handles reading data from various sources (e.g., CSV files), splitting datasets into training and testing sets, and saving the results. The `DataIngestionConfig` class stores configuration parameters, while the `DataIngestion` class performs the ingestion process, ensuring data is ready for analysis.

- **Data Transformation**: 
  - **File**: `data_transformation.py`
  - Focuses on feature engineering and data cleaning, including handling missing values and feature scaling. The transformation process uses `SimpleImputer` for missing values and `StandardScaler` for feature scaling. A pipeline is created to streamline these processes.

- **Exploratory Data Analysis (EDA)**: 
  - Involves analyzing the dataset characteristics, checking for missing values, duplicates, and data types, and creating new features such as total and average scores.

- **Model Training**: 
  - **File**: `model_trainer.py`
  - This phase involves training multiple models (e.g., Linear Regression, Decision Trees, Random Forest, XGBoost) and performing hyperparameter tuning to optimize performance. The `ModelTrainer` class handles data splitting, model training, evaluation, and saving the best-performing model to a pickle file.

- **Prediction Pipeline**: 
  - **File**: `app.py`
  - Implements a Flask web application to serve predictions, allowing users to input data and receive model predictions. The application loads preprocessor and model pickle files and processes incoming requests.

## Technologies Used

- **Languages**: Python
- **Frameworks**: Flask for web application
- **Libraries**: 
  - Pandas for data manipulation
  - Scikit-learn for machine learning tasks
  - XGBoost for advanced modeling
  - Logging for monitoring and debugging
- **Cloud Platforms**: 
  - AWS (Elastic Beanstalk, EC2, ECR) 
  - Azure (Web App)
- **Containerization**: Docker for building and deploying applications
- **CI/CD**: GitHub Actions for automated deployment pipelines

## Deployment

Deployment is achieved using both AWS Elastic Beanstalk and Azure Web App, employing CI/CD pipelines to automate the deployment process. Code changes trigger automatic deployments, ensuring that the application is always up to date. The project demonstrates the use of Docker for containerization, simplifying the management and deployment of applications across different environments. 

### AWS Deployment Steps
1. **Docker Setup**: Create a Dockerfile to define the application environment.
2. **Elastic Container Registry (ECR)**: Push the Docker image to ECR.
3. **EC2 Instance**: Launch an EC2 instance with Docker installed.
4. **GitHub Actions**: Configure GitHub Actions to automate the deployment process.

### Azure Deployment Steps
1. **Azure Web App**: Set up an Azure Web App for hosting the application.
2. **GitHub Actions**: Configure GitHub Actions to trigger deployment upon code updates.

## Features

- **Exploratory Data Analysis (EDA)**: Comprehensive analysis of dataset characteristics, including visualizations.
- **Model Evaluation**: Evaluate model performance using metrics such as R² score and cross-validation.
- **Logging and Error Handling**: Implement robust logging and custom exception handling for better monitoring.
- **Prediction Interface**: A user-friendly interface for making predictions through a web application, enabling easy interaction with the model.

## Getting Started

1. Clone the repository.
2. Set up the environment with the necessary dependencies listed in `requirements.txt`.
3. Configure AWS or Azure credentials for deployment.
4. Follow the instructions in the documentation to run the application locally or deploy it to the cloud.

## Conclusion

This project serves as a comprehensive guide to building and deploying machine learning applications using modern software engineering practices. It provides valuable insights into the MLOps lifecycle, ensuring that machine learning models are developed, tested, and deployed in a streamlined and efficient manner.
