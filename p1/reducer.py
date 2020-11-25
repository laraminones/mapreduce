#!/usr/bin/env python

actual_city = None
actual_max_tmp = "-9999.0"
actual_min_tmp = "9999.0"
city = ""

for line in sys.stdin:
	line = line.strip()

	city,max_tmp,min_tmp = line.split("\t",2)

	if actual_city == None:
		actual_max_tmp = max_tmp
		actual_min_tmp = min_tmp
	else:
		if actual_city == city:
			if float(max_tmp) > float(actual_max_tmp):
				actual_max_tmp = max_tmp
			if float(min_tmp) < float(actual_min_tmp):
				actual_min_tmp = min_tmp
		else:
			print("%s\t%s\t%s" % (actual_city, actual_max_tmp, actual_min_tmp))
			actual_max_tmp = max_tmp
			actual_min_tmp = min_tmp
	actual_city = city

if actual_city == city:
	print("%s\t%s\t%s" % (actual_city, actual_max_tmp, actual_min_tmp))