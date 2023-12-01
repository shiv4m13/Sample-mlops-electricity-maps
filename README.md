# Model Pipeline/ Architecture

## Overview

This repository contains the code and configuration for deploying a machine learning model using a continuous integration and continuous deployment (CI/CD) pipeline. The pipeline is triggered whenever a developer pushes code changes to the GitHub repository. The pipeline includes testing, building a Docker image, pushing the image to the AWS Elastic Container Registry (ECR), and updating a Lambda function linked to an AWS API Gateway.

## CI/CD Process

### 1. GitHub Actions Workflow

The CI/CD process is initiated through GitHub Actions, a CI/CD service integrated with the GitHub repository. The workflow is defined in the `.github/workflows/ci-cd.yml` file.

#### Workflow Steps:

- **On Push Event:** The workflow is triggered whenever there is a new push to the repository.

- **Test Model:** The first step involves testing the machine learning model using predefined input samples. The tests are defined in the `tests` directory, and the testing script is specified in the workflow configuration.

- **Build Docker Image:** If the tests pass successfully, the workflow proceeds to build a Docker image containing the model and its dependencies. The Docker image is defined by the `Dockerfile` in the project root.

- **Push to AWS ECR:** The built Docker image is pushed to the AWS Elastic Container Registry (ECR) for versioned storage and retrieval.

- **Update Lambda Function:** After successfully pushing the Docker image to ECR, the Lambda function is updated with the latest version of the model. This step ensures that the deployed model in the AWS Lambda environment is synchronized with the latest changes.

- **Update API Gateway:** Finally, the AWS API Gateway is updated to link it to the updated Lambda function. This step ensures that the API Gateway routes incoming requests to the correct version of the deployed model.

### 2. Docker Image

The Docker image is defined by the `Dockerfile` in the project root. It specifies the base image, installs necessary dependencies, and copies the model files into the image. This Docker image encapsulates the entire model and its runtime environment, ensuring consistency between development and deployment environments.

### 3. AWS Services

- **Elastic Container Registry (ECR):** ECR is used to store and manage Docker images. The GitHub Actions workflow pushes the built Docker image to ECR.

- **Lambda Function:** AWS Lambda is utilized to host the machine learning model. The function is updated with the latest Docker image version after successful testing and building.

- **API Gateway:** AWS API Gateway is configured to route incoming requests to the Lambda function. It is updated to link to the latest version of the Lambda function, ensuring that the deployed model is accessible through the API.


---
---


Certainly! Let's break down the detailed process of handling model drift, setting standards for folder structure, and automating the testing and deployment process.

### 1. **Handling Model Drift:**

   - **Monitoring for Drift:** Implement monitoring mechanisms within your Lambda function to detect model drift. This can involve comparing model predictions against expected outcomes or monitoring specific performance metrics.

   - **Exception or Wrong Predictions Detection:** Set up alerts or monitoring triggers to identify instances where the Lambda function generates exceptions or produces incorrect predictions. This can be based on unexpected changes in the input data distribution or model behavior.

   - **Automated Alerts:** Configure automated alerting systems to notify the team when significant drift is detected.

   - **Reverting to Previous Image:** If drift is detected, and the Lambda function is generating exceptions or incorrect predictions, have an automated process in place to revert to a previous Docker image stored in AWS ECR.


### 2. **Setting Standards for Folder Structure:**
   Creating a standardized folder structure for each new service or model not only promotes consistency but also streamlines the entire pipeline for testing and deployment.

   #### Standard Folder Structure:
   - **Test Cases Directory:** Include a directory for unit tests and integration tests to ensure the functionality of individual components and the system as a whole.
   - **Dockerfile:** Provide a Dockerfile for containerization, ensuring consistency in the deployment environment.
   - **Lambda File:** If applicable, include files for serverless deployments, such as AWS Lambda functions.
   - **CI/CD Configuration:** Automatically attach CI/CD configuration files to each repository for seamless integration into the deployment pipeline.

   #### Sample Folder Structure:
   ```
   ├── model_repo/
   │   ├── model_code/
   │   │   ├── ...
   │   ├── tests/
   │   │   ├── unit_tests/
   │   │   │   ├── ...
   │   │   ├── integration_tests/
   │   │   │   ├── ...
   │   ├── Dockerfile
   │   ├── lambda_function.py
   │   ├── .github/
   │   │   ├── workflows/
   │   │   │   ├── ci_cd.yml
   ├── ...
   ```

### 3. **Automation of Testing and Deployment:**

   #### Docker Images with AWS ECR:
   - **Docker Images:** Containerize your model and its dependencies using Docker images. This ensures consistency across different environments.
   - **AWS ECR:** Utilize AWS Elastic Container Registry (ECR) to store and manage Docker images. This facilitates easy rollback to previous images in case of issues.

   #### CI/CD Pipeline:
   - **Automatic CI/CD Attachment:** Automate the attachment of CI/CD configuration files (e.g., GitHub Actions workflow) to each repository.
   - **Testing Stages:** Define testing stages in the CI/CD pipeline, including unit tests, integration tests, and any additional validation steps.
   - **Deployment Stage:** Integrate a deployment stage that pushes the Docker image to AWS ECR and deploys it to the production environment.

By implementing these practices, you create a standardized, automated, and easily maintainable process for handling model drift, testing, and deploying new models. This approach enhances the reliability, reproducibility, and scalability of your machine learning workflows.



## Scalable and Versioned Model Deployment on AWS Lambda:
      To ensure scalable and versioned model deployment on AWS Lambda, a streamlined infrastructure can be established. AWS Lambda inherently handles scalability, automatically adjusting resources based on demand. When a new model version is ready, it can be uploaded to an Amazon S3 bucket, and Lambda can be configured to fetch the latest model from there. Utilizing AWS Lambda layers or packaging dependencies with the deployment package ensures consistency across versions. Furthermore, by integrating with a version control system like Git and an Amazon ECR registry, updates can be triggered automatically. When a new model version is pushed to the ECR registry, a CI/CD pipeline can be set up to deploy the updated Lambda function seamlessly, ensuring that the latest models are readily available without manual intervention. This approach simplifies the deployment process and promotes scalability while accommodating future model updates effortlessly.


## Monitoring Metrics

- **Invocation Count and Duration:** Monitor Lambda invocation count and duration.

- **Error Rates:** Track error rates in Lambda invocations.

- **S3 Bucket Metrics:** Monitor S3 bucket metrics for efficient model updates.

- **API Gateway Latency:** Assess API Gateway latency for end-to-end performance.

- **Resource Utilization:** Monitor Lambda resource utilization for optimal performance.

- **Cost Metrics:** Track Lambda function costs for financial insights.


# Future Enhancements

## Microservices Architecture with Kubernetes

If you find yourself with additional time and resources, exploring Kubernetes for a microservices architecture can be a beneficial endeavor. This move holds the potential to greatly enhance scalability and flexibility, especially as our model count continues to grow. Delving into Kubernetes allows for a more sophisticated deployment infrastructure.

## Efficient Model Versioning with S3 Buckets

Consider incorporating Amazon S3 buckets into our deployment strategy to store model weights. This enhancement provides a robust solution for efficient model versioning and management. Taking this step can contribute to a more streamlined and organized approach as we handle an increasing number of models.



## Request Code:

```
import requests
import json

# Specify the path to the JSON file containing input data
json_file_path = "<json_file_path>"

# Read the input data from the JSON file
with open(json_file_path, 'r') as file:
    input_data = json.load(file)

# URL of the API endpoint you want to send the request to
api_url = "https://7yjy2qj96c.execute-api.us-east-1.amazonaws.com/testing2"

# Headers to be included in the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Send a POST request to the specified API endpoint with input data and headers
response = requests.post(api_url, json=input_data, headers=headers)

# Check the HTTP status code of the response
if response.status_code == 200:
    # If the response status code is 200, print the result obtained from the API
    result = response.json()
    print("Result:", result)
else:
    # If the response status code is not 200, print an error message with the status code and response text
    print(f"Error: {response.status_code} - {response.text}")
```

# Note:
## Input JSON File Format
The input JSON file is expected to follow a specific structure with two main components: columns and data. This format is crucial for successful execution of the API request script.
```
{
   "columns": ["column1", "column2", "column3", ...],
   "data": [
      [value11, value12, value13, ...],
      [value21, value22, value23, ...],
      ...
   ]
}
```
