#!/usr/bin/env python3

import os
import sys

for line in sys.stdin:
	city_name = os.environ["map.input.file"]
	
	line = line.strip()
	words = line.split()
	max_tmp = words[5]
	min_tmp = words[6]

	if max_tmp != "-9999.0":
		print("%s\t%s\t%s" % (city_name,max_tmp,min_tmp))