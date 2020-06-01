from setuptools import setup

setup(
   name='EC2Snapshotter',
   version='0.1',
   author='Ronnie Hyslop',
   author_email='ronnie.hyslop@nucleusfinancial.com',
   description='EC2Snapshotter is a tool to manage AWS EC2 snapshots',
   license='GPLv3+',
   packages=['snapshotter'],
   url='https://github.com/nuc-ronniehyslop/ec2-snapshotter',
   install_requires=[
      'click',
      'boto3'
   ],
   entry_points='''
      [console_scripts]
      snapshotter=snapshotter.snapshotter:cli
   ''',
)