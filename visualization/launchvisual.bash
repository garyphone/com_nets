#!/bin/bash

# This script is used to convert the xml to 1 yaml file and 2 json files

python xml2json.py

echo -ne '####                      (25%)\r'
sleep 1

python xml2yaml.py

echo -ne '########                  (50%)\r'
sleep 1

. demo-openrc.sh

echo -ne '############              (75%)\r'
sleep 1

FILENAME="TEST"

openstack stack create --template launch.yaml $FILENAME

echo -ne '#################   (100%)\r'
echo -ne '\n'

sleep 3

openstack stack list

echo 'Congratulation! You have created a stack'
