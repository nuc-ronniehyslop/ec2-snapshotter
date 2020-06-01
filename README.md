# ec2-snapshotter

Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

snapshotter uses IAM Instance role.

## Running

`pipenv run "python snapshotter/snapshotter.py <command> <subcommand> <--project=PROJECT>"`

*command* is instances, volumes or snapshots
*subcommand* depends on command
*project* is optional