#!/usr/bin/env python

import json

_f = raw_input()
f = json.loads(_f)

with open('/home/ubuntu/garbage/' + f['data']['id'],'w+') as out:
    out.write(_f)

print f['data']['link']
