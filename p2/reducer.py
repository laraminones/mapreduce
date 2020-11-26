#!/usr/bin/env python

import sys

#user o url
#files o numero de veces que aparece la url
actual_user = None
actual_files = 0
user = None

for line in sys.stdin:
    line = line.strip()

    user,files = line.split('\t',1)

    try:
        files = int(files)
    except ValueError:
        continue

	if user == None:
        if actual_user:
            print('%s\t%d' % (actual_user, actual_files))
        actual_user = user
        actual_files = files
    else:
        actual_files = files+1

if actual_user == user:
    print('%s\t%d' % (actual_user, actual_files))
