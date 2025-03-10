# Exceptions are of 2 types: API (BotoCore) & Service (AWS Resources)(Need to store the error first to find out if it was due to a service or not)
# Need to import botocore.exceptions
# There are very generic errors, in most cases we get ClientError

# Boto3 Session: 
# Client created in a session will have the same region and credentials as the session but if we specify in the client we create, it will overwrite it
# Session basically is a extra layer, transfer s3 bucket form region to another region and create a automation for this, so we would need to assume roles in both regions.
# Not thread safe

