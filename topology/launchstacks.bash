#!/bin/bash

# This script is used to convert the xml to yaml and then launch the stacks in the OpenStack

python xml2yaml.py

. demo-openrc.sh

FILENAME="TEST"

openstack stack create --template launch.yaml $FILENAME

