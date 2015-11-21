import json
import os

FILEPATH = 'reminders.json'


def load_json():
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, 'w+') as fw:
            fw.write('{}')
    return json.load(open(FILEPATH, 'r'))


def dump_json(content):
    with open(FILEPATH, 'w+') as fp:
        json.dump(content, fp)


def get_max(d, kword):
    if d.keys():
        return int(max(d.keys()).lstrip(kword))
    else:
        return -1
