# Udacity-Developing-Your-First-ML-Workflow
This is the Github repo for Udacity Developing your first ML workflow course. This repo contains the code for demos, exercises and the final project.  

---  

# **👉 Project 2 Submission: Build a ML Workflow For Scones Unlimited On Amazon SageMaker**  

A CIFAR image classification workflow on AWS    
Udacity AWS Machine Learning Engineer Nanodegree (ND189)     

🟢 **Watch [the project demo video](https://youtu.be/TxnJmCHKoqY)** [(Project notes)](https://docs.google.com/document/d/1FqwqBpwTXh0J3NofO0v3uxq15RGns1Gd_ukteuP827A)      

* Step 1, data staging  
    * [Starter notebook](https://github.com/nov05/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/starter.ipynb) 
* Step 2, modeling training / deployment
    * Refer to the starter notebook   
* Step 3, Lambda functions and Step Functions workflow
    * [Lambda function Python scripts](https://github.com/nov05/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/lambda.py)    
    * [State machine JSON script](https://github.com/nov05/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/project/Udacity_P2_CIFAR.json) 
* Step 4, testing and evaluation
    * Refer to the starter notebook
    
<br>  

* The state machine  
<img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/Udacity/20241119_aws-mle-nanodegree/2024-11-26%2020_20_29-Settings.jpg" width=600>  

* The state machine workflow consists of 3 Lambda functions: 
    * `Udacity_P2_GetData` selects a random data point from the test dataset, encodes it, and passes it to the next Lambda function.
    * `Udacity_p2_Predict` decodes the data, gets an inference from the trained image classification model, and passes the inference to the next Lambda function.  
    * `Udacity_P2_Threshold` compares the inference to the threshold — if it's above, the workflow proceeds to the end. If not, it raises an exception, which is caught by the state machine and routed to the end of the workflow.   

* Graph of the flow: 
    * above the threshold vs. below the threshold  
    <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/Udacity/20241119_aws-mle-nanodegree/stepfunctions_graph%20(1).png" width=150> <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/Udacity/20241119_aws-mle-nanodegree/stepfunctions_graph.png" width=150>

* Evaluation plot:
    * So far all the inferences are above the threshold.  
    <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/Udacity/20241119_aws-mle-nanodegree/output.png" width=400>

👉 Others

* AWS Machine Learning Workflow: **Lambda Function** for Preprocessing  
    * [Video walkthrough](https://youtu.be/IFAxlL1ntb8)  
    * [texts and screenshots](https://docs.google.com/document/d/1UIvKF1TWEuyh_h8WI-ciNGdwTzQOp5fpOMSAf22Truo)     

* AWS Machine Learning Workflow: **Step Functions** for Preprocessing and Training workflow
    * [Video walkthrough](https://youtu.be/6iYb4k1OQqE)  
    * [texts and screenshots](https://docs.google.com/document/d/1Um47l8guJbz3r_OnQyV1aTgI_93fkWcyiUI3xig-cmQ)  
  
<br>
<br>  
 
---  

## Folder Structure
This repo contains a folder for each lesson and one project folder.

## Lessons Folder
Each lesson folder contains files for exercises and demos. The exercise code should contain instructions necessary for the exercises along with the solution. The demo code contains the files the instructor uses in the lesson demos.

## Project Folder
The project folder contains all files and instructions necessary for the project.