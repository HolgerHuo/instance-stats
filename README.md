# Island 岛屿 Stats bot

![GitHub last commit](https://img.shields.io/github/last-commit/holgerhuo/instance-stats)![GitHub release (latest by date)](https://img.shields.io/github/v/release/holgerhuo/instance-stats)![GitHub](https://img.shields.io/github/license/holgerhuo/instance-stats)![GitHub all releases](https://img.shields.io/github/downloads/holgerhuo/instance-stats/total)![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/holgerhuo/instance-stats)

The [Island 岛屿](https://mast.dragon-fly.club) [statistic bot](https://mast.dragon-fly.club/@islandstats). 

Install Python 3 and requirements and set a cronjob to run whenever you want to post statistics.

`pip3 install -r requirements.txt`

An example configuration file named `config.py` is below.

Placeholders are in `%%...%%`, feel free to edit them

```
client_id=""
client_secret=""
access_token=""
instance="https://mast.dragon-fly.club"
visibility="unlisted"
show_change=True
text = """
#island岛屿晚间播报 #islandstats 
晚上好~各位islanders
目前本实例的版本号为: %%version%%.
共有 %%usercount%% 位超可爱的你们发出了 %%statuscount%% 条嘟嘟
我们共发现了 %%domaincount%% 个实例并和他们发出了友好互动

期待与各位Islanders一同创造的明天~
"""
```
