from backend import TOKEN

import json
import requests

def get_points():
    r = requests.get("https://dt.miet.ru/ppo_it_final", headers={"X-Auth-Token": TOKEN})
    if r.status_code != 200:
        raise requests.ConnectionError("Can't get data from api")

    return json.loads(r.text)["message"]
