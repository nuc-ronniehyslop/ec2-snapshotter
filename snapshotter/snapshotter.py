import boto3
import click

session = boto3.Session()
ec2 = session.resource('ec2')


@click.command()
def list_instances():
    "List EC2 Instances"
    for i in ec2.instances.all():
        name = ''
        for tag in i.tags:
            if tag['Key'] == 'Name':
                name = tag['Value']
      
            
        print(', '.join((
            i.id,
            name, 
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
    return


if __name__ == '__main__':
    list_instances()
