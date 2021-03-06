#!/usr/bin/python 

import subprocess as sp 
import json 
import os 
from user_information.user_info import USERNAME

log_file_path = "/home/{}/aws-ec2-slackbot/src/logs/instances.json".format(USERNAME)

def create_log_with_all_ec2_instances(keypair, profile):
	sp.call("aws ec2 describe-instances --filters \"Name=key-name, Values={}\" --profile {} > {}".format(keypair, profile, log_file_path), shell=True)
	data         = json.load(open(log_file_path)) 
	reservations = data["Reservations"]
	print("{} reservations found".format(len(reservations)))
	return reservations

def find_running_ec2_instances(reservations):
	instances                = [instance for instance_list in [reservation.get("Instances") for reservation in reservations] for instance in instance_list]
	running_instances        = [ (instance.get("InstanceId"), instance.get("State").get("Name")) for instance in instances if instance.get("State").get("Name") == "running"]
	ids_of_running_instances = [ instance_id[0] for instance_id in running_instances]
	no_of_running_instances  = len(running_instances)
	print("{} instances found".format(len(instances)))
	print("{} EC2 instance(s) currently running".format(no_of_running_instances))
	return no_of_running_instances, ids_of_running_instances

