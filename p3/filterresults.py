#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_files', nargs='+', type=str, help='path')
args = parser.parse_args()

for file in args.input_files:
    with open(file, 'r') as input_file:
        for line in input_file.readlines():
            parts = line.split("\t")
            print('Los factores de calidad para el vino %s son %s' % (parts[0], " ".join(parts[1:])))

  