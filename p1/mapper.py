#!/usr/bin/env python

import os
import sys

for line in sys.stdin:
	city_name = os.environ["mapreduce_map_input_file"]

	line = line.strip()
	words = line.split()
	max_tmp = words[5]
	min_tmp = words[6]

	aux_city = city_name.split('/')
	city = aux_city[-1]

	if (max_tmp != "-9999.0" and min_tmp != "-9999.0"):
		print('%s\t%s\t%s' % (city_name,max_tmp,min_tmp))
