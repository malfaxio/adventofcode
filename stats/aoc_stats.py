#!/usr/bin/env python3

import json

with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)