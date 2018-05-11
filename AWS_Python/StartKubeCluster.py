import boto3


## the following code will create AWS ec2 instance.

ec2=boto3.resource('ec2')

ec2.instances.filter(InstanceIds=['i-064436aa3d857b577','i-07acb96d22fb79a4b','i-0fd68d922936c53b9']).start()    ## statement to start the existing instances

