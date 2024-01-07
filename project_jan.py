import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response ['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running' and instance['InstanceId'] == 'i-0a5aba3aeb59c98b6':
                             print(instance['InstanceId'])
    response2 = ec2.stop_instances(
                                        InstanceIds = [instance['InstanceId'],
                
        ],
        
    )
    def get_instance_ids(instance_names):
        print(response2)
    
                
            
        

