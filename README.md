# ec2-snapshotter

Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

snapshotter uses IAM Instance role.

## Running

`pipenv run "python snapshotter/snapshotter.py <command> <--project=PROJECT>"`

*command* is list, start or stop
*project* is optional