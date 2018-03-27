#!/usr/bin/env python

import json
import os

# Usage: COLOR=blue ./app.py

# parse data file
with open('data.json', 'r') as f:
    data = json.load(f)

print('%-15s%-15s' % ('USER', 'COLOR'))

# find required COLOR
color = os.getenv('COLOR')
for item in data:
    if item['color'] == color:
        print('%-15s%-15s' % (item['user'], item['color']))
