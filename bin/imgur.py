#!/usr/bin/env python

import json

f = raw_input()
f = json.loads(f)

print f['data']['link']
