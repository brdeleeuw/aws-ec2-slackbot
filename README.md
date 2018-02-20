# aws-ec2-slackbot

Simple bot for the Slack messaging app that checks for active EC2 instances (Amazon Web Services) and sends a reminder.

Requirements:

- Python 2.7
- Slackclient Python module
- Slack account / workspace
- Amazon Web Services (AWS) account 
- AWS Command Line Interface (CLI) configured


Adjust slack_credentials_example.py file and add your auth token. Save as slack_credentials.py

Adjust user_info_example.py and add the names of your AWS profiles and your keypair-username combinations as shown in the example. Save as user_info.py.


Example crontab entry to send a reminder at 16:30, 17:00 and 17:30 every day:

```
#min    #hour   day-of-month    month   day-of-week     commannd
30       16           *             *        *        cd /home/<user>/slack_bot/src/ && /usr/bin/python /home/<user>/slack_bot/src/run_bot.py  >> /home/<user>/slack_bot/src/logs/run_bot_output.txt  2>&1
00       17           *             *        *        cd /home/<user>/slack_bot/src/ && /usr/bin/python /home/<user>/slack_bot/src/run_bot.py  >> /home/<user>/slack_bot/src/logs/run_bot_output.txt  2>&1
30       17           *             *        *        cd /home/<user>/slack_bot/src/ && /usr/bin/python /home/<user>/slack_bot/src/run_bot.py  >> /home/<user>/slack_bot/src/logs/run_bot_output.txt  2>&1
```


