#!/usr/bin/python

import sys

totalValue = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# We calculate total for value

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", totalValue
        oldKey = thisKey;
        totalValue = 0

    oldKey = thisKey
    totalValue += float(thisValue)

if oldKey != None:
    print oldKey, "\t", totalValue
