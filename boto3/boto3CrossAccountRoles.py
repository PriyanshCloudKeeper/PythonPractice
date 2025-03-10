# We will create a cross account role using boto3
# Kuch bhi access karne ka leeya huma chahiye hoga access key or secret key

# sts client banaka role assume kiye or fir uska credentials aa gaye, jisko use karke hum cheeza karenga or yeh short term credentials hota hai

# we programmatically assume a aws role using boto3, so in the role what do we put in the principal? the account number of the account that we are using the credentials off?

# experiation time for temporary credentials from sts.assume_role() in boto3: 12 hr Programatically and then it can be specified when we are creating the role 1-12hr. even if we specified 1hr while creating the role. i can be used for 12hrs programatically, ie programaTICALLY WILL TAKE PRECEDENCE

import boto3

sts_client = boto3.client('sts')  # by default takes the region if not specified.

assumed_role= sts_client.assume_role(
    RoleArn = '', #the role you want to assume. (That role should have the trust and resource policy and our account should have a role that allows assuming that role)
    RoleSessionName = 'AssumeRoleSessionTest'
)

# We are account B trying to assume account A right
# Basically we are allowing to assume the role programatically, so if it was the console, we would create a role in B that allows stsassumerole:rolecreatedinA, so basically it is that but pogramatically

# Assume role ka andar bohot information hai or uska andar hum credentials mai jaa rahe hai 
credentials = assumed_role['Credentials']

testsession = boto3.Session(
     aws_access_key_id = credentials['AccessKeyId'],
     aws_secret_access_key = credentials['SecretAccessKey'],
     aws_session_token = credentials['SessionToken']
)

ec2_client = boto3.client('ec2', region_name='ap-south-1') # we need to specify the region
response = ec2_client.describe_instances()

# transitive switching: first account sa third account (using second account in between), used in WARs 
# Legal confused deputy is transitive switching?
# premission boundary