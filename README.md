# aws-ec2-slackbot
<<<<<<< HEAD
Simple bot for the Slack messaging app that checks for active EC2 instances (Amazon Web Services) and sends a reminder.

Prerequisites:
SlackClient

Example crontab entry to send a reminder at 16:30. 17:00 and 17:30 every day:

`
#min    #hour   day-of-month    month   day-of-week     commannd
30       16           *             *        *        cd /home/<user>/slack_bot/src/ && /usr/bin/python /home/<user>/slack_bot/src/run_bot.py  >> /home/<user>/slack_bot/src/logs/run_bot_output.txt  2>&1

00       17           *             *        *        cd /home/<user>/slack_bot/src/ && /usr/bin/python /home/<user>/slack_bot/src/run_bot.py  >> /home/<user>/slack_bot/src/logs/run_bot_output.txt  2>&1

30       17           *             *        *        cd /home/<user>/slack_bot/src/ && /usr/bin/python /home/<user>/slack_bot/src/run_bot.py  >> /home/<user>/slack_bot/src/logs/run_bot_output.txt  2>&1
`

=======
Simple bot for the Slack messaging app that checks for active EC2 instances  (Amazon Web Services) and can send reminders. 
>>>>>>> 6827e21147398dc579a10d67db2b117f0dd288da
