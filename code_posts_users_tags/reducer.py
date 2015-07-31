#!/usr/bin/python
import sys
import operator

def get_by_val(dictionary, val):
    for key in dictionary:
        if dictionary[key] == val:
            return key
    return None

old_tag = None
q_num = 0
top_tags = {}

for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    tag, one = data_mapped

    if old_tag and old_tag != tag:
        if len(top_tags.keys()) < 10:
            top_tags[old_tag] = q_num
        else:
            min_top = min(top_tags.values())
            if q_num > min_top:
                min_top_tag = get_by_val(top_tags, min_top)
                del top_tags[min_top_tag]
                top_tags[old_tag] = q_num
        q_num = 0

    old_tag = tag
    q_num += 1

sorted_tags = sorted(top_tags.items(), key=operator.itemgetter(1), reverse=True)
for tag in sorted_tags:
    print "{0}\t{1}".format(tag[0], tag[1])
