# Client = ?
# When you explicitly set keys and region for the client, and when you accidently push the code to GitHub, the key will not work as AWS will automatically expire it
# Client ek bar mai ek hee jagha sa cheeza laa skata hai: region specific. Jab tak service global na hoo
# what will happen if you do not pass SessionToken while temporary credentitals in boto3: Temporary credentials will not work
# MissingSessionTokenError?
# Precedence between the default region in cred file and the one specified when creating client: the one specified when creating client will take precedence and if not specified the default region in cred file will be used

# Generic nameing convention: list (high level), describe (specific information), read, delete, update

import boto3

# s3_client= boto3.client('s3')
# s3_client = boto3.client('s3', region_name='us-east-1', aws_access_key_id='XXXXXXXXXXXXXXXXXXXX', aws_secret_access_key='ZQZJZQZJZQZJZQZJZQZJZQZJZQZJZQZJZQZJZQZJ')

ec2_client = boto3.client('ec2', region_name='ap-south-1')

# Refer to boto3 docs for ec2, goto your usecase and just copy paste
# How to check which parameter is required or not? -> documentation mai info hogyi kii kya kya required hai or kya prameter kya karta hai?
# DryRun: Check permissions without actually running the operation (API call hogyi par execute nahi hoga, bus ek dry run hoga)

response = ec2_client.describe_instances() # Can specify filters inside () like dry run, can specify AZs
print(response)
print('\n')

# Suppose if we don't have any instanes in that region, then what to do?

# Learn Parsing : Data extratcion from JSON

# We just want ec2 name and id
for i in response ['Reservations']:
    for j in i['Instances']:
        print(j['InstanceId'], j['InstanceType'])

# Paginators: used for processing large amounts of returned data, if pagination is not available for a specific api thenwe can create our custom pagenation using next_token

# Waiters: used to poll (request) a specific API and when it completes the specific filter we set, and then an event is raised.

# Logging: enables logging for your application debugging processes.

