#!/usr/bin/python

from bot import *
from aws_functions import * 
from user_information.user_info import last_names_and_keypairs, profiles
import datetime

def main():
	for user in last_names_and_keypairs:
		keypair   = user["keypair"]
		last_name = user["last_name"]
		for profile in profiles:
			reservations             = create_log_with_all_ec2_instances(keypair, profile)
			no_of_running_instances  = find_running_ec2_instances(reservations)[0]
			ids_of_running_instances = find_running_ec2_instances(reservations)[1]
			
			if no_of_running_instances  == 1:
				MESSAGE = "Keypair `{}` has {} running EC2 instance with id `{}`".format(keypair, no_of_running_instances, ids_of_running_instances[0] )
			elif no_of_running_instances > 1:
				MESSAGE = "Keypair `{}` has {} running EC2 instances with ids `{}`".format(keypair, no_of_running_instances, ids_of_running_instances)
			elif no_of_running_instances == 0:
				continue
			slack_user_id         = get_slack_user_id(last_name)
			slack_user_channel_id = get_slack_user_channel_id(slack_user_id)
			send_slack_message(slack_user_channel_id, MESSAGE)
			
			try: 
				print("{}\n{}\n{}\n{}\n".format(datetime.datetime.now(), keypair, slack_user_id, slack_user_channel_id))
			except:
				continue

if __name__ == "__main__":
    main()


