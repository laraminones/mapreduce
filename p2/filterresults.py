#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_files', nargs='+', type=str, help='path')
args = parser.parse_args()

max_hits = 0
max_url = ""

for file in args.input_files:
    with open(file, 'r') as input_file:
        for line in input_file.readlines():
            row = line.split('\t')
            max_hits_acu = int(row[1])
            if max_hits_acu > max_hits:
                max_hits = max_hits_acu
                max_url = row[0]

print('La url con más hits es %s con %d hits.' % (max_url,max_hits))
