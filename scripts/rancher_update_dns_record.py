"""
Updates the type A DNS record of the lightsail.conatest.click zone handled
by Lightsail
"""

from os import environ
from json import dumps
import boto3

session = boto3.Session(
    aws_access_key_id=environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=environ['AWS_SECRET_ACCESS_KEY']
)
client = session.client('lightsail')


def get_instance_by_name(name: str):
    """ Gets an instance object by name """
    instances = client.get_instances().get('instances')
    for instance in instances:
        if instance['name'] == name:
            return instance


def get_entry_by_name(domainName: str, name: str):
    """ Gets a domain entry by name """
    response = client.get_domain(domainName=domainName)
    entries = response['domain']['domainEntries']
    for entry in entries:
        if entry['name'] == name:
            return entry


def print_dict(dictionary: dict):
    """ Prints a dictionary to the console """
    print(dumps(dictionary, indent=2, default=str))


if __name__ == '__main__':
    instance = get_instance_by_name('rancher_server')

    domain_name = 'lightsail.conatest.click'
    name = instance['name'] + '.' + domain_name
    public_ip_address = instance['publicIpAddress']

    try:
        response = client.create_domain_entry(
            domainName=domain_name,
            domainEntry={
                'name': name,
                'target': public_ip_address,
                'type': 'A',
            }
        )
    except Exception as e:
        domain_entry = get_entry_by_name(domain_name, name)
        domain_entry['target'] = public_ip_address

        response = client.update_domain_entry(
            domainName=domain_name,
            domainEntry=domain_entry
        )

    print_dict(response)
