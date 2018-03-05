#!/bin/pathon

import random
import os
import json

count = os.getenv("FILE_COUNT") or 100
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

'''
id = 1
while if < count:
'''

# range gives a numerable off upper bound that is known:

for identifier in range(1, count + 1):
    amount = random.uniform(1.0, 1000.0)
    content = {
            'topic': random.choice(words),
            'value': "%.2f" % amount
            #       ^^^ string with float and 2 decimal points
            }
    with open('./new/receipt-%s.json' % identifier, 'w') as f:
        json.dump(content, f)


