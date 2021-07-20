#!/usr/bin/python3
from mastodon import Mastodon
import psutil
import creds
import sys
from datetime import datetime

client = Mastodon(
  client_id=creds.client_id,
  client_secret=creds.client_secret,
  access_token=creds.access_token,
  api_base_url=creds.instance
)
me = client.account_verify_credentials()

instance = client.instance()
time = datetime.utcnow().strftime("%Y-%m%-d %H:%I:%S")

text = """
koyu.space is currently running version %%version%%.
There are %%usercount%% users registered who posted %%statuscount%% statuses.
We are currently federating with %%domaincount%% domains.
Our CPU load is %%cpu%% and the RAM is at %%ram%%.
These stats have been noted at %%timestamp%% UTC.

#koyustats :pb:
"""

text = text.replace("%%version%%", instance.version)
text = text.replace("%%usercount%%", str(instance.stats.user_count))
text = text.replace("%%statuscount%%", str(instance.stats.status_count))
text = text.replace("%%domaincount%%", str(instance.stats.domain_count))
text = text.replace("%%cpu%%", str(int(psutil.cpu_percent()))+"%")
text = text.replace("%%ram%%", str(int(psutil.virtual_memory().percent))+"%")
text = text.replace("%%timestamp%%", time)

dryrun = False
try:
  if sys.argv[1] == "--dry-run":
    dryrun = True
except:
  pass

if not dryrun:
  client.toot(text)
else:
  print(text)