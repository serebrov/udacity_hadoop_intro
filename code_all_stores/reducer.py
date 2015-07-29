#!/usr/bin/python

import sys

salesTotal = 0
salesNum = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# We need to find sales total and number of sales for each store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    salesTotal += float(thisSale)
    salesNum += 1

print salesTotal, "\t", salesNum

