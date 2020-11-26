#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_files', nargs='+', type=str, help='path')
args = parser.parse_args()

max_tmp = -9999.9
min_tmp = 9999.9
max_city = ""
min_city = ""

for file in args.input_files:
    with open(file, 'r') as input_file:
        for line in input_file.readlines():
            row = line.split('\t')
            max_tmp_acu = float(row[1])
            min_tmp_acu = float(row[2])
            if max_tmp_acu > max_tmp:
                max_tmp = max_tmp_acu
                max_city = row[0]
            if min_tmp_acu < min_tmp:
                min_tmp = min_tmp_acu
                min_city = row[0]

print('El lugar en el que hizo más calor fue %s con %s grados.' % (max_city,max_tmp))
print('El lugar en el que hizo más frío fue %s con %s grados.' % (min_city,min_tmp))
