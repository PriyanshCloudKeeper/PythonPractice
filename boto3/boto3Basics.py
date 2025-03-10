# Offical AWS SDK for Python (Boto3 is a wrapper around the AWS SDK for Python (Boto Core))

# aws cli - ./aws/ contains config (region and output format) and contains credentials (aws access key and secret key)
# if we skip region and format, the config file will not be made
# Credentials file is used for storing sensitive information like access key and secret key
# Config files contain insensitive information like region and output format, it also contains boto3 realted information.
# Boto3 only supports json output

# There are 2 ways to fetch information: client (gets the most detailed, but less readable) and resource (gets less detailed info, but more readable)

import boto3

S3_RESOURCE = boto3.resource('s3')

print("My S3 Resource: ")
for bucket in S3_RESOURCE.buckets.all():
    print(bucket.name)

print("My S3 Objects: ")
for obj in S3_RESOURCE.Bucket('my-amazon-s3-bucket-for-ck-exercise').objects.all():
    print(obj.key)
    