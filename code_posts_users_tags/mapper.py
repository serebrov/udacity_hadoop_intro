#!/usr/bin/python
"""

"id": id of the node
"title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
"tagnames": space separated list of tags
"author_id": id of the author
"body": content of the post
"node_type": type of the node, either "question", "answer" or "comment"
"parent_id": node under which the post is located, will be empty for "questions"
"abs_parent_id": top node where the post is located
"added_at": date added

We are interested seeing what are the top tags used in posts.

Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

NOTE: current implementation can be improved. Now mappers output all the tags and then reducers process all the data.
Instead mapper can pre-process the data and return only top 10 tags.
Then reducer will have much less job to do.
"""

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    # post data
    post_id, title, tagnames, user_id, body, node_type = data[:6]
    parent_id, abs_parent_id, added_at, score = data[6:10]

    if post_id == 'id':
        continue

    if node_type == "question":
        tags = tagnames.split(" ")
        for tag in tags:
            print "{0}\t1".format(tag)
