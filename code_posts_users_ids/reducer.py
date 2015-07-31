#!/usr/bin/python
import sys

old_id = None
users = []

for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    post_id, user_id = data_mapped

    if old_id and old_id != post_id:
        print old_id, "\t", "\t".join(users)
        users = []

    old_id = post_id
    users.append(user_id)

if old_id:
    print old_id, "\t", "\t".join(users)
