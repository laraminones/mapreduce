#!/usr/bin/env python

import os
import sys

for line in sys.stdin:
    wine = os.environ['mapreduce_map_input_file'].split('/')[-1].split('.')[0]
    line = line.strip()
    words = line.split(';')
    words = ('\t').join(words)
    print('%s\t%s' % (wine,words))
