#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_files', nargs='+', type=str, help='path')
args = parser.parse_args()

max_wine = None

for file in args.input_files:
    with open(file, 'r') as input_file:
        for line in input_file.readlines():
            if max_wine == None:
                row = line.split('\t')
                acu = float(row[13])
                wine = row[0]
                max_wine=wine
                quality = row[1:13]
                try:
                    quality = [float(atr) for atr in quality]
                except ValueError:
                    continue
                max_quality1 = ""
                for atr in quality:
                    max_quality1 = max_quality1+" "+str(atr/acu)
            else:
                row = line.split('\t')
                acu = float(row[13])
                wine = row[0]
                quality = row[1:13]
                try:
                    quality = [float(atr) for atr in quality]
                except ValueError:
                    continue
                max_quality2=""
                for atr in quality:
                    max_quality2 = max_quality2+" "+str(atr/acu)

print('Los factores de calidad para el vino %s son %s' % (wine,max_quality2))
print('Los factores de calidad para el vino %s son %s' % (max_wine,max_quality1))
