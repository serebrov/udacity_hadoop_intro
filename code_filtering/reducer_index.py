#!/usr/bin/python

import sys

oldWord = None
nodes = set()
total = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    word, node = data_mapped

    if oldWord and oldWord != word:
        print oldWord, "\t", total, "\t", ','.join(map(lambda i: str(i), sorted(nodes)))
        nodes = set()
        total = 0

    oldWord = word
    try:
        nodes.add(int(node))
        total += 1
    except:
        pass

if oldWord != None:
    print word, "\t", total, "\t", ','.join(map(lambda i: str(i), sorted(nodes)))
