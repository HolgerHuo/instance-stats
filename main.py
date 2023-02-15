#!/usr/bin/python3
from mastodon import Mastodon
import requests
import config
import json
import os
import sys
from datetime import datetime

client = Mastodon(
  access_token=config.access_token,
  api_base_url=config.toot_instance
)
text = config.text

time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

instance = requests.get(config.source_instance+'/api/v1/instance').json()

mau = requests.get(config.source_instance+'/api/v2/instance').json()['usage']['users']['active_month']


if not config.show_change or not os.path.exists('db.json'):
  text = text.replace("%%version%%", instance['version'])
  text = text.replace("%%usercount%%", str(instance['stats']['user_count']))
  text = text.replace("%%statuscount%%", str(instance['stats']['status_count']))
  text = text.replace("%%domaincount%%", str(instance['stats']['domain_count']))
  text = text.replace("%%timestamp%%", time)
  text = text.replace("%%mau%%", str(mau))
else:
  
  f = open('db.json', 'r')
  db = json.loads(f.read())
  f.close()
  
  domain_change = instance['stats']['domain_count']-db["domain_count"]
  status_change = instance['stats']['status_count']-db["status_count"]
  user_change = instance['stats']['user_count']-db["user_count"]
  mau_change = mau - db['mau']

  if instance['version'] == db["version"]:
    text = text.replace("%%version%%", instance['version'])
  else:
    text = text.replace("%%version%%", db["version"] + "➡" + instance['version'])
  text = text.replace("%%usercount%%", str(instance['stats']['user_count']) + '(%+-d)'%user_change)
  text = text.replace("%%statuscount%%", str(instance['stats']['status_count']) + '(%+-d)'%status_change)
  text = text.replace("%%domaincount%%", str(instance['stats']['domain_count']) + '(%+-d)'%domain_change)
  text = text.replace("%%timestamp%%", time)
  text = text.replace("%%mau%%", str(mau) + '(%+-d)'%mau_change)

db={'version':instance['version'],'user_count':instance['stats']['user_count'],'status_count':instance['stats']['status_count'],'domain_count': instance['stats']['domain_count'], 'mau': mau}
db = json.dumps(db)
f = open('db.json', 'w')
f.write(db)
f.close()

dryrun = False
try:
  if sys.argv[1] == "--dry-run":
    dryrun = True
except:
  pass

if not dryrun:
  client.status_post(text, visibility=config.visibility)
else:
  print(text)