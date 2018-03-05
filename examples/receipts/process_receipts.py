#!/bin/python
import glob
import os
import shutil
import json
# adding regular expressions
import re
#this is for subtotal:
import math

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")


rcpts = [f for f in glob.iglob('./new/receipt-[0-9]*.json')
        if re.match('./new/receipt-[0-9]*[02468].json', f)]

subtotal = 0.0

for path in rcpts:
    with open(path) as f:
        content = json.load(f)
        subtotal += math.ceil(float(content['value']))
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)
    print("moved '%s' to '%s'" % (path, destination))


print("Receipt subtotal is: $%s " % round(subtotal,2))

