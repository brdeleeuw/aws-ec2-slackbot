# aws-ec2-slackbot

Simple bot for the Slack messaging app that checks for active EC2 instances (Amazon Web Services) and sends a reminder.

Requirements:

- Python 2.7
- Slackclient Python module
- Slack account / workspace
- Amazon Web Services (AWS) account 
- AWS Command Line Interface (CLI) configured


Adjust ```slack_credentials_example.py``` file and add your auth token. Save as ```slack_credentials.py```

Adjust ```user_info_example.py```:

- Add the username on your operating system
- Add the names of your AWS profiles 
- Add the keypair-username combinations as shown in the example. 

Save as ```user_info.py```.

Adjust USERNAME in the ```aws_functions.py```

To make the run_bot.py file executable, cd into the directory and make it executable:

```cd ~slack_bot/src
chmod +x run_bot.py```

To send reminders, we can have the file run in a cronjob.

```crontab -e```

Then add whenever you want the file to run. Example of a crontab entry to send a reminder at 16:30, 17:00 and 17:30 every day:

```
#min    #hour   day-of-month    month   day-of-week     commannd
30       16           *             *        *        cd ~/slack_bot/src/ && /usr/bin/python ~/slack_bot/src/run_bot.py  >> ~/slack_bot/src/logs/run_bot_output.txt  2>&1
00       17           *             *        *        cd ~/slack_bot/src/ && /usr/bin/python ~/slack_bot/src/run_bot.py  >> ~/slack_bot/src/logs/run_bot_output.txt  2>&1
30       17           *             *        *        cd ~/slack_bot/src/ && /usr/bin/python ~/slack_bot/src/run_bot.py  >> ~/slack_bot/src/logs/run_bot_output.txt  2>&1
```


