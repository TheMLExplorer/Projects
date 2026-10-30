print("hi")
# Experiment 1: Set Up a Git Repository and Push It to GitHub
# Step 1: Create a project folder
# Open VS Code terminal and execute:
# mkdir DataScienceProject
# cd DataScienceProject


# -Step 2: Initialize Git
# git init

# Step 4: Check repository status
# git status

# Step 5: Add files to the staging area
# git add .

# Step 6: Commit the changes
# git commit -m "Initial commit"


# Step 8: Connect local repository to GitHub
# Replace YOUR_USERNAME with your GitHub username.
# git branch -M main
# git remote add origin https://github.com/YOUR_USERNAME/DataScienceProject.git


# Step 9: Push project to GitHub
# git push -u origin main


# Step 10: Track future changes
# Whenever you modify your Python code, execute:
# git status
# git add .
# git commit -m "Update project code"
# git push

# To configure your Git username and email, use these commands in the VS Code terminal.
# 1. Set Git username
# git config --global user.name "TheMLExplorer"


# 2. Set Git email
# git config --global user.email "your-github-email@gmail.com"


# Replace the email with the email associated with your GitHub account.
# 3. Verify configuration
# git config --global user.name
# git config --global user.email


# 4. Check all Git configurations
# git config --list

###################################################################################################################################################
# Experiment 2: All Git Commands in Step-by-Step Order
# Aim: Create feature branches, merge them, resolve conflicts, and push the project to GitHub.

# Step 1: Create project folder
# mkdir DataScienceProject
# cd DataScienceProject


# Step 2: Initialize Git
# git init


# Step 3: Configure Git username and email
# (Only required if you have not configured them previously.)
# git config --global user.name "TheMLExplorer"
# git config --global user.email "your-github-email@gmail.com"


# Step 4: Create Python file
# Create main.py and write:
# print("Welcome to Data Science Project")



# Step 5: Add and commit files
# git add .
# git commit -m "Initial commit"


# Step 6: Create first feature branch
# git switch -c feature1


# Modify main.py:
# print("Welcome to Data Science Project")print("Feature 1: Data Cleaning")



# Save and commit:
# git add .
# git commit -m "Add data cleaning feature"


# Step 7: Create second feature branch
# git switch main
# git switch -c feature2


# Modify the same main.py:
# print("Welcome to Data Science Project")print("Feature 2: Data Visualization")



# Save and commit:
# git add .
# git commit -m "Add data visualization feature"


# Step 8: Switch to main branch
# git switch main


# Step 9: Merge first branch
# git merge feature1


# Step 10: Merge second branch
# git merge feature2


# Possible merge conflict
# Because both branches changed the same line, Git may show a conflict.
# Step 11: Resolve merge conflict
# Open main.py. You may see:
# <<<<<<< HEADprint("Feature 1: Data Cleaning")=======print("Feature 2: Data Visualization")>>>>>>> feature2



# Remove the conflict markers and keep both features:
# print("Welcome to Data Science Project")print("Feature 1: Data Cleaning")print("Feature 2: Data Visualization")



# Save the file.
# Step 12: Complete conflict resolution
# git add .
# git commit -m "Resolve merge conflict"


# Step 13: Check branches
# git branch


# Step 14: Check commit history
# git log --oneline --all --graph


# Step 15: Connect GitHub repository
# First, create an empty repository named DataScienceProject on GitHub.

# Then execute:
# git remote add origin https://github.com/YOUR_USERNAME/DataScienceProject.git


# Step 16: Push project to GitHub
# git push -u origin main

####################################################################################################################

# Practical3: Fork an AI Project, Create a Feature Branch, Push Changes and Create a Pull Request
# Step 1: Create a folder and open it
# mkdir DataScienceP
# cd DataScienceP


# If the folder already exists, don't create it again. Just enter it:
# cd DataScienceP


# Step 2: Clone the open-source repository
# git clone https://github.com/dhruvTerminal/iris-classification-sklearn.git


# Enter the repository:
# cd iris-classification-sklearn


# Check repository status:
# git status


# Step 3: Configure Git
# git config --global user.name "TheMLExplorer"
# git config --global user.email "your-github-email@gmail.com"


# Check configuration:
# git config --global user.name
# git config --global user.email


# Step 4: Create a feature branch
# git switch -c feature-update


# Check branches:
# git branch


# Expected output:
# * feature-update
#   main


# Step 5: Open the project in VS Code
# code .


# Create a new file named evaluation.py and write:
# from sklearn.metrics import accuracy_score, f1_scorey_actual = [1, 0, 1, 1, 0]y_predicted = [1, 0, 1, 0, 0]accuracy = accuracy_score(y_actual, y_predicted)f1 = f1_score(y_actual, y_predicted)print("Accuracy:", accuracy)print("F1 Score:", f1)



# Save the file.
# Step 6: Add and commit changes
# Check modified files:
# git status


# Add files:
# git add .


# Commit changes:
# git commit -m "Add model evaluation metrics"


# Step 7: Fork the repository on GitHub
# This step is performed on the GitHub website, not in PowerShell.
# 1. Open Original Iris Repository.
# 2. Click Fork.
# 3. Select your GitHub account (TheMLExplorer).
# 4. Click Create fork.
# Step 8: Configure remote repositories
# Set your fork as origin:
# git remote set-url origin https://github.com/TheMLExplorer/iris-classification-sklearn.git


# Add the original repository as upstream:
# git remote add upstream https://github.com/dhruvTerminal/iris-classification-sklearn.git


# Check remote URLs:
# git remote -v


# Expected output:
# origin    https://github.com/TheMLExplorer/iris-classification-sklearn.git (fetch)
# origin    https://github.com/TheMLExplorer/iris-classification-sklearn.git (push)

# upstream  https://github.com/dhruvTerminal/iris-classification-sklearn.git (fetch)
# upstream  https://github.com/dhruvTerminal/iris-classification-sklearn.git (push)


# Step 9: Push your feature branch
# git push -u origin feature-update


# This uploads your feature branch to your GitHub fork.
# Step 10: Create a Pull Request
# This step is also performed on GitHub.
# 1. Open your fork: TheMLExplorer/iris-classification-sklearn.
# 2. Select the feature-update branch.
# 3. Click Compare & pull request.
# 4. Check the following:
# Option	Repository / Branch
# Base repository	dhruvTerminal/iris-classification-sklearn
# Base branch	main
# Head repository	TheMLExplorer/iris-classification-sklearn
# Compare branch	feature-update

# 5. Click Create pull request.
# Step 11: Get updates from the original repository
# If the original repository has new changes, download them:
# git fetch upstream


# Switch to your feature branch:
# git switch feature-update


# Merge the original repository's main branch:
# git merge upstream/main


# If a merge conflict occurs, open the conflicting file in VS Code and resolve the conflict markers.

# Then run:
# git add .
# git commit -m "Resolve merge conflict"


# Push the updated feature branch:
# git push origin feature-update
################################################################################################################################################################################################################

# Practical 4: Research and Explain How DevOps Principles Like CI/CD Can Improve Deployment and Updates for Machine Learning Projects
# 1. Aim
# To study how DevOps principles, especially Continuous Integration (CI) and Continuous Deployment (CD), improve the deployment, testing, and updating of Machine Learning (ML) projects.
# 2. What is DevOps?
# DevOps is a combination of Development and Operations.

# It is a process that helps developers build, test, deploy, and maintain software faster and more reliably.

# In Machine Learning, DevOps helps us manage the complete ML model lifecycle, from development to deployment and monitoring.
# 3. What is CI/CD?
# CI/CD stands for Continuous Integration and Continuous Delivery/Deployment.

# 1. Continuous Integration (CI)
# - Developers regularly add code to a shared repository.
# - Code is automatically tested.
# - Errors are detected early.
# - It improves code quality.
# 2. Continuous Deployment (CD)
# - After successful testing, changes can be automatically deployed.
# - New ML models can be released to users.
# - It makes updates faster and easier.
# 4. How does CI/CD work in an ML project?
# Example: We develop a Machine Learning model to predict house prices.
# 1. Code Development

# Develop ML model using Python


# 2. GitHub

# Upload code to repository


# 3. Continuous Integration (CI)

# Automatically test code and validate data


# 4. Model Training and Evaluation

# Train model and check accuracy


# 5. Continuous Deployment (CD)

# Deploy the tested model


# 6. Monitoring

# Monitor model performance and errors


# 5. How DevOps improves ML projects
# 1. Faster deployment: Models can be deployed automatically.
# 2. Better quality: Automatic testing helps find errors.
# 3. Easy updates: New code and models can be updated quickly.
# 4. Team collaboration: Multiple developers can work together.
# 5. Monitoring: Model performance can be monitored after deployment.
# 6. Reliability: Previous model versions can be restored if a new version fails.
# 6. Tools used in DevOps and ML
# Tool	Purpose
# Git	Version control
# GitHub	Store and share code
# Jenkins	Automate CI/CD
# Docker	Package applications
# MLflow	Track ML experiments and models
# Kubernetes	Manage deployed containers

# 7. Real-life example
# Suppose we create a house-price prediction model.
# - First, we develop the model using Python.
# - We upload the code to GitHub.
# - Jenkins automatically runs tests.
# - If tests pass, the model is deployed.
# - If we improve the model, the new version can be deployed automatically.
# - We monitor its performance after deployment.
# This saves time and reduces manual work.
# 8. Conclusion
# DevOps and CI/CD make Machine Learning projects faster, more reliable, and easier to maintain. They automate testing, deployment, updating, and monitoring of ML models.

###################################################################################################################################################################################


# Practical 5: Jenkins Setup with GitHub (Short Steps)
# Step 1: Install requirements
# - Install Java JDK 21 or later.
# - Install Jenkins.
# - Install Git and Python.
# Step 2: Start Jenkins
# Open browser:
# http://localhost:8080


# Complete Jenkins setup and install suggested plugins.
# Step 3: Create an AI/DS project
# Open PowerShell:
# mkdir MLProject
# cd MLProject
# code .


# Step 4: Create Python file
# Create test.py:
# def add(a, b):    return a + bassert add(2, 3) == 5print("All tests passed!")



# Step 5: Create Jenkinsfile
# Create a file named Jenkinsfile:
# pipeline {
#     agent any

#     stages {
#         stage('Build') {
#             steps {
#                 echo 'Building ML Project'
#             }
#         }

#         stage('Test') {
#             steps {
#                 bat 'python test.py'
#             }
#         }

#         stage('Deploy') {
#             steps {
#                 echo 'Deployment completed'
#             }
#         }
#     }
# }


# Step 6: Upload project to GitHub
# Create a GitHub repository named MLProject.

# Run:
# git init
# git add .
# git commit -m "Initial commit"
# git branch -M main
# git remote add origin https://github.com/TheMLExplorer/MLProject.git
# git push -u origin main


# Step 7: Configure Jenkins
# 1. Open Jenkins (localhost:8080).
# 2. Click New Item.
# 3. Enter MLProject.
# 4. Select Pipeline → OK.
# 5. Select Pipeline script from SCM.
# 6. Select Git.
# 7. Enter your GitHub repository URL.
# 8. Set branch to */main.
# 9. Set Script Path to Jenkinsfile.
# 10. Click Save.
# Step 8: Enable GitHub Webhook
# 1. Open Jenkins job → Configure.
# 2. Enable GitHub hook trigger for GITScm polling.
# 3. Save.
# 4. Open GitHub repository → Settings → Webhooks → Add webhook.
# 5. Enter your publicly accessible Jenkins webhook URL:
# https://YOUR-PUBLIC-JENKINS-ADDRESS/github-webhook/


# 6. Select application/json.
# 7. Select Just the push event.
# 8. Click Add webhook.
# Note: GitHub cannot send webhooks directly to localhost. Jenkins must be reachable through a secure public server or tunnel.
# Step 9: Test the pipeline
# Make a change in test.py, then run:
# git add .
# git commit -m "Update code"
# git push origin main


# Jenkins should automatically start a new build.
# Step 10: Check output
# Open Jenkins → MLProject → Build History → Console Output.

# Expected output:
# Building ML Project
# All tests passed!
# Deployment completed
# Finished: SUCCESS


# # Result: Jenkins is configured to automatically build and test the AI/DS project whenever new code is pushed to GitHub.

# 13. Viva Questions and Answers
# Q1. What is Jenkins?

# Ans: Jenkins is an open-source automation tool used for CI/CD.

# Q2. What is a Jenkins pipeline?

# Ans: A Jenkins pipeline is a sequence of automated stages used to build, test, and deploy software.

# Q3. What is a webhook?

# Ans: A webhook sends an automatic notification from GitHub to Jenkins when an event occurs.

# Q4. What is a Jenkinsfile?

# Ans: Jenkinsfile is a file that contains pipeline instructions.

# Q5. What is the use of GitHub in Jenkins?

# Ans: GitHub stores the project code, and Jenkins retrieves it to run automated builds and tests.

# Q6. What is the benefit of automated builds?

# Ans: They save time and help detect errors quickly.

# Q7. What is CI/CD?

# Ans: CI means Continuous Integration, and CD means Continuous Delivery or Continuous Deployment.

# Q8. What is Console Output?

# Ans: It displays the logs and results of a Jenkins build.
##########################################################################################################################

# Practical 6: Create a Docker Container for an AI Model and Test It Locally
# 1. Aim
# To create a Docker container for a Machine Learning model and test it on a local machine.
# 2. Requirements
# - Python
# - VS Code
# - Docker Desktop
# - Scikit-learn
# 3. Step-by-step process
# Step 1: Install Docker
# Download and install Docker Desktop.

# Open Docker Desktop and start it.

# Check installation:
# docker --version


# Step 2: Create project folder
# mkdir DockerML
# cd DockerML
# code .


# Step 3: Create Python file (app.py)
# from sklearn.linear_model import LinearRegressionmodel = LinearRegression()model.fit([[1], [2], [3]], [2, 4, 6])prediction = model.predict([[4]])print("Predicted Value:", prediction[0])



# Step 4: Create requirements.txt
# scikit-learn


# Step 5: Create Dockerfile
# Create a file named Dockerfile (without extension).
# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY app.py .

# CMD ["python", "app.py"]


# Step 6: Build Docker image
# Run in the project terminal:
# docker build -t my-ai-model .


# Step 7: Run Docker container
# docker run --name ai-container my-ai-model


# Step 8: Check container
# docker ps -a


# Step 9: Remove container (optional)
# docker rm ai-container


# 4. Expected output
# Predicted Value: 8.0


# Result
# Successfully created a Docker image and container for a Machine Learning model and tested it locally.
# 5. Important Docker commands
# Command	Purpose
# docker --version	Check Docker version
# docker build	Create Docker image
# docker images	List images
# docker run	Run container
# docker ps	Show running containers
# docker ps -a	Show all containers
# docker rm	Remove container
# docker rmi	Remove image

# 6. Viva Questions
# Q1. What is Docker?

# Ans: Docker is a platform used to package applications with their dependencies.

# Q2. What is a Docker image?

# Ans: An image is a package used to create containers.

# Q3. What is a Docker container?

# Ans: A container is a running instance of a Docker image.

# Q4. What is a Dockerfile?

# Ans: A Dockerfile contains instructions to build a Docker image.

# Q5. Why use Docker in Machine Learning?

# Ans: It helps run ML models consistently across different environments.

# Q6. What is the difference between an image and a container?

# Ans: An image is a template, while a container is an instance created from that image.

###############################################################################################################################

# Practical 7: Use Docker Compose to Manage Multiple Containers for a Web-Based AI Application
# 1. Aim
# To use Docker Compose to manage multiple containers for a web-based AI application, including AI model, database, and frontend containers.
# 2. Requirements
# - Python
# - VS Code
# - Docker Desktop
# - Docker Compose
# - Flask
# 3. Step-by-step process
# Step 1: Create project folder
# mkdir AIWebApp
# cd AIWebApp
# code .


# Step 2: Create project structure
# Create these files:
# AIWebApp/
# │
# ├── app.py
# ├── requirements.txt
# ├── Dockerfile
# └── docker-compose.yml


# Step 3: Create AI model and backend (app.py)
# from flask import Flask, jsonifyfrom sklearn.linear_model import LinearRegressionapp = Flask(__name__)model = LinearRegression()model.fit([[1], [2], [3]], [2, 4, 6])@app.route("/")def home():    prediction = model.predict([[4]])[0]    return jsonify({"prediction": prediction})if __name__ == "__main__":    app.run(host="0.0.0.0", port=5000)



# Step 4: Create requirements.txt
# flask
# scikit-learn


# Step 5: Create Dockerfile
# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY app.py .

# CMD ["python", "app.py"]


# Step 6: Create docker-compose.yml
# This file manages three services: AI model, database, and frontend.
# services:

#   ai-model:
#     build: .
#     ports:
#       - "5000:5000"

#   database:
#     image: postgres:15
#     environment:
#       POSTGRES_USER: admin
#       POSTGRES_PASSWORD: password123
#       POSTGRES_DB: aidb
#     ports:
#       - "5432:5432"

#   frontend:
#     image: nginx:alpine
#     ports:
#       - "8080:80"
#     depends_on:
#       - ai-model
#       - database


# Note: This is a basic demonstration. The frontend is an Nginx container, and the database is PostgreSQL. They are started together, but this example does not yet connect the frontend to the AI API or store predictions in the database.
# Step 7: Start all containers
# Run:
# docker compose up --build


# Step 8: Check running containers
# Open another terminal:
# docker compose ps


# Step 9: Test the AI model
# Open your browser:
# http://localhost:5000


# Expected output:
# {
#   "prediction": 8.0
# }


# Open the frontend:
# http://localhost:8080


# Step 10: Stop all containers
# docker compose down


# 4. Important Docker Compose commands
# Command	Purpose
# docker compose up	Start all containers
# docker compose up --build	Build and start containers
# docker compose ps	Show container status
# docker compose logs	Display logs
# docker compose down	Stop and remove containers
# docker compose restart	Restart services

# 5. Conclusion
# Docker Compose helps manage multiple containers together. It simplifies running an AI model, database, and frontend as one application.
# 6. Viva Questions and Answers
# Q1. What is Docker Compose?

# Ans: Docker Compose is a tool used to manage multiple Docker containers together.

# Q2. What is a container?

# Ans: A container is an isolated environment in which an application runs.

# Q3. What is the use of docker-compose.yml?

# Ans: It defines services, images, ports, and configurations for containers.

# Q4. Why do we use multiple containers?

# Ans: To separate the frontend, backend AI model, and database.

# Q5. What is PostgreSQL?

# Ans: PostgreSQL is an open-source relational database.

# Q6. What is the difference between Docker and Docker Compose?

# Ans: Docker manages individual containers, while Docker Compose manages multiple containers together.

#######################################################################################################################################

# Practical 8: Set Up a Local Kubernetes Cluster with Minikube to Deploy and Scale a Dockerized AI Application
# 1. Aim
# To set up a local Kubernetes cluster using Minikube and deploy and scale a Dockerized AI application.
# 2. Requirements
# - Docker Desktop
# - Minikube
# - kubectl
# - VS Code
# - Dockerized AI application
# 3. Step-by-step process
# Step 1: Install Minikube
# Download and install Minikube.

# Install kubectl.

# Check installation:
# minikube version
# kubectl version --client


# Step 2: Start Minikube cluster
# minikube start --driver=docker


# Check cluster:
# kubectl get nodes


# Step 3: Create AI application
# Create a folder:
# mkdir K8sAI
# cd K8sAI
# code .


# Create app.py:
# from flask import Flaskapp = Flask(__name__)@app.route("/")def home():    return "AI Model is Running!"if __name__ == "__main__":    app.run(host="0.0.0.0", port=5000)



# Step 4: Create requirements.txt
# flask


# Step 5: Create Dockerfile
# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY app.py .

# EXPOSE 5000

# CMD ["python", "app.py"]


# Step 6: Build Docker image inside Minikube
# minikube image build -t ai-model:v1 .


# Step 7: Create Kubernetes deployment file
# Create deployment.yaml:
# apiVersion: apps/v1
# kind: Deployment

# metadata:
#   name: ai-deployment

# spec:
#   replicas: 2

#   selector:
#     matchLabels:
#       app: ai-model

#   template:
#     metadata:
#       labels:
#         app: ai-model

#     spec:
#       containers:
#       - name: ai-container
#         image: ai-model:v1
#         imagePullPolicy: IfNotPresent
#         ports:
#         - containerPort: 5000


# Step 8: Deploy the application
# kubectl apply -f deployment.yaml


# Check deployment:
# kubectl get deployments


# Check pods:
# kubectl get pods


# Step 9: Expose the application
# Create service.yaml:
# apiVersion: v1
# kind: Service

# metadata:
#   name: ai-service

# spec:
#   type: NodePort
#   selector:
#     app: ai-model

#   ports:
#   - port: 5000
#     targetPort: 5000
#     nodePort: 30001


# Apply service:
# kubectl apply -f service.yaml


# Open application:
# minikube service ai-service


# Expected output in browser:
# AI Model is Running!


# Step 10: Scale the application
# Increase replicas from 2 to 4:
# kubectl scale deployment ai-deployment --replicas=4


# Check pods:
# kubectl get pods


# You should see four AI application pods when all are ready.
# Step 11: Delete deployment and service
# kubectl delete -f service.yaml
# kubectl delete -f deployment.yaml


# Stop Minikube:
# minikube stop


# 4. Important Kubernetes commands
# Command	Purpose
# minikube start	Start cluster
# kubectl get nodes	Show cluster nodes
# kubectl apply -f	Deploy configuration
# kubectl get pods	Show pods
# kubectl get deployments	Show deployments
# kubectl get services	Show services
# kubectl scale	Increase or decrease replicas
# kubectl delete -f	Delete resources
# minikube stop	Stop cluster

# 5. Conclusion
# Minikube creates a local Kubernetes cluster. Kubernetes helps deploy, manage, and scale Dockerized AI applications using multiple pods.
# 6. Viva Questions and Answers
# Q1. What is Kubernetes?

# Ans: Kubernetes is an open-source platform used to manage and scale containers.

# Q2. What is Minikube?

# Ans: Minikube runs a local Kubernetes cluster on a computer.

# Q3. What is a Pod?

# Ans: A Pod is the smallest deployable unit in Kubernetes. It contains one or more containers.

# Q4. What is a Deployment?

# Ans: A Deployment manages application pods and their replicas.

# Q5. What is scaling?

# Ans: Scaling means increasing or decreasing the number of application replicas.

# Q6. What is kubectl?

# Ans: kubectl is a command-line tool used to communicate with Kubernetes.

# Q7. What is a Service?

# Ans: A Service provides a stable way to access application pods.

# Q8. What is Minikube used for?

# Ans: It is used to learn and test Kubernetes locally.

#######################################################################################################################################

# Practical 9: Implement Auto-Scaling for an AI App on Kubernetes and Monitor Its Health and Performance Metrics
# 1. Aim
# To implement automatic scaling of an AI application on Kubernetes and monitor its health and performance.
# 2. Requirements
# - Docker Desktop
# - Minikube
# - kubectl
# - Metrics Server
# - Dockerized AI application
# 3. Step-by-step process
# Step 1: Start Minikube
# minikube start --driver=docker


# Step 2: Enable Metrics Server
# minikube addons enable metrics-server


# Check metrics:
# kubectl top nodes


# Step 3: Deploy AI application
# Create a file named deployment.yaml:
# apiVersion: apps/v1
# kind: Deployment
# metadata:
#   name: ai-deployment
# spec:
#   replicas: 2
#   selector:
#     matchLabels:
#       app: ai-model
#   template:
#     metadata:
#       labels:
#         app: ai-model
#     spec:
#       containers:
#       - name: ai-container
#         image: ai-model:v1
#         imagePullPolicy: IfNotPresent
#         ports:
#         - containerPort: 5000
#         resources:
#           requests:
#             cpu: "100m"
#           limits:
#             cpu: "500m"


# Apply deployment:
# kubectl apply -f deployment.yaml


# Step 4: Create a Horizontal Pod Autoscaler (HPA)
# Create a file named autoscale.yaml:
# apiVersion: autoscaling/v2
# kind: HorizontalPodAutoscaler
# metadata:
#   name: ai-hpa
# spec:
#   scaleTargetRef:
#     apiVersion: apps/v1
#     kind: Deployment
#     name: ai-deployment
#   minReplicas: 2
#   maxReplicas: 5
#   metrics:
#   - type: Resource
#     resource:
#       name: cpu
#       target:
#         type: Utilization
#         averageUtilization: 50


# Apply autoscaling:
# kubectl apply -f autoscale.yaml


# Step 5: Check auto-scaling status
# kubectl get hpa


# Step 6: Monitor application health
# Check pods:
# kubectl get pods


# Check CPU and memory usage:
# kubectl top pods


# Check node performance:
# kubectl top nodes


# Check application logs:
# kubectl logs deployment/ai-deployment


# Step 7: Generate load to test scaling
# Open another PowerShell terminal and run:
# kubectl run load-generator --image=busybox:1.36 --restart=Never -- /bin/sh -c "while true; do wget -q -O- http://ai-service:5000; done"


# This command assumes you already created a Kubernetes Service named ai-service for your application.

# Watch scaling:
# kubectl get hpa -w


# The number of replicas may increase when CPU usage goes above the target, provided the application receives enough CPU load.
# Step 8: Stop load generator
# kubectl delete pod load-generator


# Step 9: Clean up
# kubectl delete -f autoscale.yaml
# kubectl delete -f deployment.yaml
# minikube stop


# 4. Important commands
# Command	Purpose
# minikube start	Start Kubernetes
# kubectl apply -f	Apply configuration
# kubectl get hpa	Check autoscaling
# kubectl get pods	Check pods
# kubectl top pods	Monitor CPU and memory
# kubectl top nodes	Monitor node resources
# kubectl logs	View application logs
# kubectl scale	Manually scale replicas

# 5. Conclusion
# Successfully configured Kubernetes Horizontal Pod Autoscaler (HPA) to automatically increase or decrease AI application replicas based on CPU utilization. Monitored application health, CPU usage, memory usage, and logs.
# 6. Viva Questions and Answers
# Q1. What is auto-scaling?

# Ans: Auto-scaling automatically increases or decreases application resources based on demand.

# Q2. What is HPA?

# Ans: HPA stands for Horizontal Pod Autoscaler. It automatically adjusts the number of pods.

# Q3. What is Metrics Server?

# Ans: It collects CPU and memory usage information from Kubernetes nodes and pods.

# Q4. What is CPU utilization?

# Ans: It is the percentage of CPU resources being used.

# Q5. Why is monitoring important?

# Ans: Monitoring helps identify errors and performance problems.

# Q6. What is the difference between manual scaling and auto-scaling?

# Ans: Manual scaling is done by a user, while auto-scaling happens automatically based on defined conditions.

# Q7. What is a replica?

# Ans: A replica is an additional running copy of an application pod.
# Practical result
# Successfully implemented auto-scaling and monitored the health and performance of a Dockerized AI application using Kubernetes.

##################################################################################################################################################

# Practical 10: Complete Step-by-Step Installation and Setup Process
# Follow these steps in order to create a CI/CD pipeline using Jenkins, Docker, and Kubernetes for your AI project.
# Step 1: Install Java
# 1. Open Java JDK Download.
# 2. Download JDK 21 or later for Windows.
# 3. Install it.
# 4. Open PowerShell and check:
# java -version


# Step 2: Install Git
# 1. Open Git Download.
# 2. Download Git for Windows.
# 3. Install using the default settings.
# 4. Check:
# git --version


# Step 3: Install Python
# 1. Open Python Download.
# 2. Download Python.
# 3. During installation, select Add Python to PATH.
# 4. Check:
# python --version


# Step 4: Install Docker Desktop









# Docker Desktop
# Download Docker Desktop

# 1. Download Docker Desktop for Windows.
# 2. Install it.
# 3. Restart your computer if required.
# 4. Open Docker Desktop and wait until it shows that Docker is running.
# 5. Check:
# docker --version


# Step 5: Install Minikube









# Minikube
# Minikube installation guide

# 1. Open the installation guide.
# 2. Select Windows.
# 3. Follow the Windows installation instructions.
# 4. Check:
# minikube version


# Step 6: Install kubectl









# kubectl
# Download kubectl

# 1. Open the official Kubernetes installation guide.
# 2. Select Windows.
# 3. Install kubectl.
# 4. Check:
# kubectl version --client


# Step 7: Install Jenkins









# Jenkins
# Download Jenkins

# 1. Open the Jenkins download page.
# 2. Select Windows.
# 3. Download the Windows installer.
# 4. Install Jenkins.
# 5. Open your browser:
# http://localhost:8080


# 6. Complete the initial setup.
# 7. Install suggested plugins.
# Step 8: Start Kubernetes
# Open PowerShell:
# minikube start --driver=docker


# Check the cluster:
# kubectl get nodes


# Expected result: Your Minikube node should show Ready.
# Step 9: Create your AI project
# mkdir AICICD
# cd AICICD
# code .


# Create these four files:
# AICICD

# app.py

# requirements.txt

# Dockerfile

# Jenkinsfile

# deployment.yaml

# service.yaml



# app.py
# from flask import Flaskapp = Flask(__name__)@app.route("/")def home():    return "AI Model Deployed Successfully!"app.run(host="0.0.0.0", port=5000)



# requirements.txt
# flask


# Dockerfile
# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY app.py .

# EXPOSE 5000

# CMD ["python", "app.py"]


# Step 10: Create Kubernetes files
# deployment.yaml
# apiVersion: apps/v1
# kind: Deployment
# metadata:
#   name: ai-deployment
# spec:
#   replicas: 2
#   selector:
#     matchLabels:
#       app: ai-model
#   template:
#     metadata:
#       labels:
#         app: ai-model
#     spec:
#       containers:
#       - name: ai-container
#         image: ai-model:v1
#         imagePullPolicy: IfNotPresent
#         ports:
#         - containerPort: 5000


# service.yaml
# apiVersion: v1
# kind: Service
# metadata:
#   name: ai-service
# spec:
#   type: NodePort
#   selector:
#     app: ai-model
#   ports:
#   - port: 5000
#     targetPort: 5000
#     nodePort: 30001


# Step 11: Create Jenkinsfile
# pipeline {
#     agent any

#     stages {
#         stage('Checkout') {
#             steps {
#                 checkout scm
#             }
#         }

#         stage('Build Docker') {
#             steps {
#                 bat 'docker build -t ai-model:v1 .'
#             }
#         }

#         stage('Test') {
#             steps {
#                 bat 'python -c "print(\'AI Model Test Successful\')"'
#             }
#         }

#         stage('Deploy') {
#             steps {
#                 bat 'kubectl apply -f deployment.yaml'
#                 bat 'kubectl apply -f service.yaml'
#             }
#         }
#     }
# }


# Step 12: Build Docker image
# docker build -t ai-model:v1 .


# Load it into Minikube:
# minikube image load ai-model:v1


# Step 13: Upload project to GitHub
# Create a new GitHub repository called AICICD.

# Run:
# git init
# git add .
# git commit -m "Initial AI project"
# git branch -M main
# git remote add origin https://github.com/TheMLExplorer/AICICD.git
# git push -u origin main


# Step 14: Configure Jenkins
# 1. Open http://localhost:8080.
# 2. Click New Item.
# 3. Enter AICICD.
# 4. Select Pipeline.
# 5. Choose Pipeline script from SCM.
# 6. Select Git.
# 7. Enter your GitHub repository URL.
# 8. Set branch to */main.
# 9. Set Script Path to Jenkinsfile.
# 10. Click Save.
# Step 15: Run Jenkins pipeline
# Click Build Now.

# Jenkins will:
# 1. Download code from GitHub.
# 2. Build the Docker image.
# 3. Run the test stage.
# 4. Deploy the application to Kubernetes.
# Step 16: Check deployment
# kubectl get pods
# kubectl get deployments
# kubectl get services


# Open your application:
# minikube service ai-service


# Expected output:
# AI Model Deployed Successfully!

# 6. Viva Questions and Answers
# Q1. What is CI/CD?

# Ans: CI/CD automates code integration, testing, and deployment.

# Q2. What is Jenkins?

# Ans: Jenkins is an automation tool used for CI/CD.

# Q3. What is Docker?

# Ans: Docker packages applications with their dependencies.

# Q4. What is Kubernetes?

# Ans: Kubernetes manages and deploys containers.

# Q5. What is a Jenkinsfile?

# Ans: It contains instructions for the Jenkins pipeline.

# Q6. What is a Docker image?

# Ans: It is a package used to create Docker containers.

# Q7. What is Kubernetes Deployment?

# Ans: It manages application pods and replicas.

# Q8. What is the main benefit of CI/CD?

# Ans: It reduces manual work and makes deployment faster and more reliable.