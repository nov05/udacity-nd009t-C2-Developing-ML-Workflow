# Udacity-Developing-Your-First-ML-Workflow
This is the Github repo for Udacity Developing your first ML workflow course. This repo contains the code for demos, exercises and the final project.  

# **👉 Project 2: Build a ML Workflow For Scones Unlimited On Amazon SageMaker**  

CIFAR image classification workflow   
Udacity AWS Machine Learning Engineer Nanodegree    

* Step 1, data staging  
* Step 2, modeling training / deployment
    * [Starter notebook](https://github.com/nov05/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/starter.ipynb)   
* Step 3, Lambda functions and Step Functions workflow
    * [Lambda function Python scripts](https://github.com/nov05/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/lambda.py)    
    * [State machine JSON script](https://github.com/nov05/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/Udacity_P2_CIFAR.json) 
* Step 4, testing and evaluation
    * Refer to the starter notebook
    

* The state machine  
<img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/Udacity/20241119_aws-mle-nanodegree/2024-11-26%2020_20_29-Settings.jpg" width=600>  

* The state machine workflow consists of 3 Lambda functions: 
    * `Udacity_P2_GetData` gets a random datapoint from the test dataset, encodes it and pass to the next Lambda function. 
    * `Udacity_p2_Predict` decondes the data and get an inference from the trained image classification model, and pass the inference to the next Lambda function.  
    * `Udacity_P2_Threshold` compares the inference to the threshold, if it is above then to the end of the workflow, if not then raise exception. The exception will be catched by the state machine, and route it to the end of the workflow.




## Folder Structure
This repo contains a folder for each lesson and one project folder.

## Lessons Folder
Each lesson folder contains files for exercises and demos. The exercise code should contain instructions necessary for the exercises along with the solution. The demo code contains the files the instructor uses in the lesson demos.

## Project Folder
The project folder contains all files and instructions necessary for the project.
