import requests
from backend import TOKEN

r = requests.get("https://dt.miet.ru/ppo_it_final", headers={"X-Auth-Token": TOKEN})

print(r.text)
