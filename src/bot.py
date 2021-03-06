#!/usr/bin/python

from slackclient import SlackClient
from credentials.slack_credentials import auth_token
from aws_functions import * 

SLACK_TOKEN  = auth_token
slack_client = SlackClient(SLACK_TOKEN)

def get_slack_user_id(user_last_name):
    api_call = slack_client.api_call("users.list")
    user_ids = []
    for member in api_call['members']:
        if user_last_name in member.get('real_name', 'none').lower():
            user_id = member["id"]
            user_ids.append(user_id)
        else:
          continue
    if len(user_ids) == 1:
        return user_ids[0]
    else:
        print("more than one user with that last name, please check manually")

def get_slack_user_channel_id(user_slack_id):
    api_call = slack_client.api_call("im.list")
    if api_call.get('ok'):
    	channel_ids = api_call.get("ims")
    	user_channel_id = [channel_id.get("id") for channel_id in channel_ids if channel_id.get("user") == user_slack_id ]
        if len(user_channel_id) >= 1:
            return user_channel_id[0]
        else:
            return user_channel_id

def send_slack_message(user_channel_id, message, as_user=True):
	slack_client.api_call("chat.postMessage", channel=user_channel_id,
                                   text=message, as_user=False)
		

                