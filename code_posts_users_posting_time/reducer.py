#!/usr/bin/python

import sys
from collections import defaultdict

def print_max_hours(user_id, hours_posts):
    max_posts_value = max(hours_posts.values())
    max_hours = filter(
        lambda h: hours_posts[h]==max_posts_value, hours_posts)
    for hour in max_hours:
        print "{0}\t{1}".format(user_id, hour)

def reducer():
    old_id = None
    user_hours = defaultdict(int)

    for line in sys.stdin:

        # YOUR CODE HERE
        # print line
        # continue
        data_mapped = line.strip().split("\t")
        user_id, hour = data_mapped[:2]

        if old_id and old_id != user_id:
            print_max_hours(old_id, user_hours)
            old_id = user_id
            user_hours = defaultdict(int)

        old_id = user_id
        user_hours[hour] += 1

    if old_id:
        print_max_hours(user_id, user_hours)


if __name__ == "__main__":
    reducer()
