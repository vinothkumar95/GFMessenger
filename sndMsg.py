from twilio.rest import TwilioRestClient
import yaml
import time
from random import randint
from apscheduler.schedulers.blocking import BlockingScheduler
import os
from urlparse import urlparse
from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_HTTP

sched = BlockingScheduler()
_configuration = None
with open('config.yaml', 'r') as f:
	_configuration = yaml.load(f)

print _configuration['birthdays']
account_sid = _configuration['TwilioCredentials']['twilio_account_sid']
auth_token  = _configuration['TwilioCredentials']['twilio_auth_token']

messages = ['This is pythonic way of managing your girlFriend',
			'I love you',
			'Good Morning/Afternoon/Night. Sorry. Busy now! Will add some moreAI Features',
			'Busy Working!',
			'Some time I may be busy with my work or may be in the TT room!'
			'Making my machine to read your msgs and respond back!',
			'Will call you soon']

from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_HTTP

host, port = urlparse(os.environ["http_proxy"]).netloc.split(":")
Connection.set_proxy_info(
host,
int(port),
proxy_type=PROXY_TYPE_HTTP,
)

client = TwilioRestClient(account_sid, auth_token)

def pythonicWayToSolveGF():
	print("in")
	message = client.messages.create(body=messages[randint(0, len(messages)-1)], to=_configuration['phone_number']['girl_friend_number'], from_=_configuration['phone_number']['my_number'])

sched.add_job(pythonicWayToSolveGF, 'interval', seconds = 60)
sched.start()
while True:
	time.sleep(10)
sched.shutdown()