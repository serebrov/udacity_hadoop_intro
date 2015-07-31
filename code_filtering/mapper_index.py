#!/usr/bin/python
import sys
import csv
import re

# Create an index of all words with links to appropriate node ids.

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    text = line[4]
    words = re.split('\W+', text)
    words = map(lambda x: x.lower(), words)
    words = filter(lambda x: x, words)
    for w in words:
        print '{0}\t{1}'.format(w, line[0])
    # writer.writerow(line)
