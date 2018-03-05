# aws-ec2-slackbot

Simple bot I wrote to avoid having unecessary active instances on Amazon Web Services (AWS). It uses AWS CLI to check for active EC2 instances / EMR clusters and sends reminders via the Slack messaging app to the corresponding user.

## Requirements:

- Python 2.7
- Slackclient Python module 
- Slack account / workspace
- Slack API token (https://api.slack.com/)
- Amazon Web Services (AWS) account 
- AWS Command Line Interface (CLI) configured

## Configuration 

Cloning the repository into your home folder: 

```
cd ~/
git clone https://github.com/brdeleeuw/aws-ec2-slackbot
```

Ìf you don't have the Python Slackclient module:

```pip install slackclient```

Adjust ```slack_credentials_example.py``` file and add your auth token. Save as ```slack_credentials.py```

Adjust ```user_info_example.py```:

- Add the username on your operating system
- Add the names of your AWS profiles found in ```~/.aws/config``` file
- Add the keypair-username combinations as shown in the example. 
- Save as ```user_info.py```.

To make the run_bot.py file executable, cd into the directory and make it executable:

```
cd ~aws-ec2-slackbot/src
chmod +x run_bot.py
```

Also, don't remove the ```#!/usr/bin/python``` shebang at the top of the script. 

You may need to adjust the ```log_file_path``` variable in ```aws_functions.py``` to the directory where you cloned the repository to if you didn't choose the home directory.  


## Running automatically

To send reminders, we can have the file run in a cronjob.

```crontab -e```

Then add whenever you want the file to run. Example of a crontab entry to send a reminder at 16:30, 17:00 and 17:30 every day:

```
#min hour day-of-month  month  day-of-week  commannd
30    16        *         *        *         cd ~/aws-ec2-slackbot/src/ && /usr/bin/python ~/aws-ec2-slackbot/src/run_bot.py  >> ~/aws-ec2-slackbot/src/logs/run_bot_output.txt  2>&1
00    17        *         *        *         cd ~/aws-ec2-slackbot/src/ && /usr/bin/python ~/aws-ec2-slackbot/src/run_bot.py  >> ~/aws-ec2-slackbot/src/logs/run_bot_output.txt  2>&1
30    17        *         *        *         cd ~/aws-ec2-slackbot/src/ && /usr/bin/python ~/aws-ec2-slackbot/src/run_bot.py  >> ~/aws-ec2-slackbot/src/logs/run_bot_output.txt  2>&1
```

