#!/usr/bin/python3
from mastodon import Mastodon
import config
import sys
from datetime import datetime

client = Mastodon(
  client_id=config.client_id,
  client_secret=config.client_secret,
  access_token=config.access_token,
  api_base_url=config.instance
)
me = client.account_verify_credentials()

instance = client.instance()
time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

text = """
#island岛屿晚间播报 #islandstats 
晚上好~各位islanders
目前本实例的版本号为: %%version%%.
共有 %%usercount%% 位超可爱的你们发出了 %%statuscount%% 条嘟嘟
我们共发现了 %%domaincount%% 个实例并和他们发出了友好互动

期待与各位Islanders一同创造的明天~
"""

text = text.replace("%%version%%", instance.version)
text = text.replace("%%usercount%%", str(instance.stats.user_count))
text = text.replace("%%statuscount%%", str(instance.stats.status_count))
text = text.replace("%%domaincount%%", str(instance.stats.domain_count))
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