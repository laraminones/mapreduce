#!/usr/bin/env python

import sys

actual_wine = None
actual_quality = [0.0]*12
wine = ""
acu = 0.0

for line in sys.stdin:
    line = line.strip()

    mapperinfo = line.split('\t')
    wine = mapperinfo[0]
    quality = mapperinfo[1:]
    acu += 1.0

    try:
        quality = [float(atr) for atr in quality]
    except ValueError:
        continue

    if actual_wine != wine:
        if actual_wine != None:
            str_acu = str(acu)
            str_actual_quality = [str(atr) for atr in actual_quality]
            str_actual_quality = ('\t').join(str_actual_quality)
            data = str_actual_quality+'\t'+str_acu
            print('%s\t%s' % (actual_wine,data))
            acu = 1.0
        actual_wine = wine
        actual_quality = quality
    else:
        actual_quality = [x + y for x, y in zip(actual_quality, quality)]

if actual_wine == wine:
    str_actual_quality = [str(atr) for atr in actual_quality]
    str_actual_quality = ('\t').join(str_actual_quality)
    str_acu = str(acu)
    data = str_actual_quality+'\t'+str_acu
    print('%s\t%s' % (actual_wine,data))
