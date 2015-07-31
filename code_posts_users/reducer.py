#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

old_id = None
user_data = None

def reducer():
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in sys.stdin:

        # YOUR CODE HERE
        # print line
        # continue
        data_mapped = line.strip().split("\t")
        user_id, record_type = data_mapped[:2]

        if record_type == "A":
            user_data = data_mapped

        if record_type == "B":
            if user_data[0] != data_mapped[0]:
                raise Exception(
                    'User %s and post data %s do not match' % (user_data, line))
            data_mapped.extend(user_data[2:])
            writer.writerow(data_mapped)
            #print line[2], "\t", user_data[2]

if __name__ == "__main__":
    reducer()
