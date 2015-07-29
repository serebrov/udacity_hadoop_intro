#!/usr/bin/python

import sys

totalValue = 0
oldKey = None

maxValue = 0
maxPath = ''

# Loop around the data
# It will be in the format key\tval
# We find only the filepath with max number of hits, result is one line

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        if totalValue > maxValue:
            maxValue = totalValue
            maxPath = oldKey
        oldKey = thisKey
        totalValue = 0

    oldKey = thisKey
    totalValue += float(thisValue)

if oldKey != None:
    if totalValue > maxValue:
        maxValue = totalValue
        maxPath = oldKey

print maxPath, "\t", maxValue
