#!/usr/bin/python3
from mastodon import Mastodon
import psutil
import os
import creds

client = Mastodon(
  client_id=creds.client_id,
  client_secret=creds.client_secret,
  access_token=creds.access_token,
  api_base_url=creds.instance
)
me = client.account_verify_credentials()