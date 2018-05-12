import boto3


# the following code will create AWS ec2 instance.

# execute the below command from the CLI to verify if the account belong to 7900
# aws sts get-caller-identity --output text --query 'Account'

# execute the above command from the CLI to verify if the account belog to 7900

ec2=boto3.resource('ec2')

ec2.instances.filter(InstanceIds=['i-0a95bb6b4274b996a','i-0adcec283a3b3f94a']).start()

# statement to start the existing instances
