
#############################################################
## Step Functions state machine: Udacity_P2_CIFAR
#############################################################
'''
input payload:
{
  "s3_bucket": "sagemaker-us-east-1-807711953667",
  "endpoint_name": "image-classification-2024-11-27-08-01-07-231",
  "threshold": 0.93
}
'''



#############################################################
## Udacity_P2_GetData
#############################################################
'''
test data:
{
    "s3_bucket": "sagemaker-us-east-1-807711953667"
}
'''
import boto3
import random
import json
import base64

def lambda_handler(event, context):
    s3_bucket = event['s3_bucket']
    s3 = boto3.resource('s3')
    # Randomly pick from the test folder in the bucket
    s3_objects = s3.Bucket(s3_bucket).objects.filter(Prefix='test')
    # Grab any random object key from that folder!
    s3_key = random.choice([x.key for x in s3_objects])
    ## Read the binary data
    image_data = s3.Object(
        bucket_name=s3_bucket, 
        key=s3_key).get()['Body'].read()  
    image_data = base64.b64encode(image_data).decode('utf-8')
    event['s3_key'] = s3_key
    event['image_data'] = image_data
    event['inference'] = ""
    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }



#############################################################
## Udacity_P2_Predict
#############################################################
'''
test data:
{
  "s3_bucket": "sagemaker-us-east-1-807711953667",
  "s3_key": "test/minibike_s_002227.png",
  "image_data": "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",
  "endpoint_name": "image-classification-2024-11-26-21-33-53-998",
  "inference": ""
}
dict format to JSON:
{
  "body": "{\"s3_bucket\": \"sagemaker-us-east-1-807711953667\",\"s3_key\": \"test/minibike_s_002227.png\",\"image_data\": \"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\",\"endpoint_name\": \"image-classification-2024-11-26-21-33-53-998\",\"inference\": \"\"}"
}
'''
import json
import base64
import boto3

def lambda_handler(event, context):
    print(event)
    event = json.loads(event['body'])
    image_data = event['image_data']
    endpoint_name = event['endpoint_name']

    image = base64.b64decode(image_data.encode('utf-8'))
    sagemaker_runtime = boto3.client("sagemaker-runtime")
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name, 
        ContentType="image/png", 
        Body=image
    )
    event['inference'] = json.loads(response['Body'].read().decode('utf-8'))  ## convert to list
    event['image_data'] = ''  ## clear image data
    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }



#############################################################
## Udacity_P2_Threshold
#############################################################
'''
test data:
{
  "inference": [
    0.9986796975135803,
    0.0013202379923313856
  ],
  "threshold": 0.93
}
dict format to JSON:
{
  "body": "{\"inference\": [0.9986796975135803, 0.0013202379923313856], \"threshold\": 0.93}"
}
'''
import json

def lambda_handler(event, context):
    print(event)
    event = json.loads(event['body'])
    inference = event['inference']
    threshold = event['threshold']

    # Grab the inferences from the event
    # Check if any values in our inferences are above threshold
    meets_threshold = (
        inference[0]>=threshold or inference[0]<=1-threshold
    )
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise Exception("⚠️ The confidence threshold was not met.")
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }