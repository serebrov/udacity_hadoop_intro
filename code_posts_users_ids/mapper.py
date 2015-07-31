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

As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.

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
        print "{0}\t{1}".format(post_id, user_id)

    if node_type == "answer":
        print "{0}\t{1}".format(parent_id, user_id)

    if node_type == "comment":
        print "{0}\t{1}".format(parent_id, user_id)
