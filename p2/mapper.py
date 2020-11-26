#!/usr/bin/env python

import sys

for line in sys.stdin:
#Divido por / para quedarme con el nombre del fichero
#Divido por . para quedarme con el usuario
#user = os.environ['mapreduce_map_input_file'].split('/')[-1].split('.')[0]
    line = line.strip()
    words = line.split()
    url = words[3]

    print('%s\t%d' % (url,1))
