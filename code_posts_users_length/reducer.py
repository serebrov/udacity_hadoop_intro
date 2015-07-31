#!/usr/bin/python
import sys

old_id = None
post_data = None
answers_num = 0
answers_len = 0


def print_data(post_data, answers_num, answers_len):
    if answers_num:
        print "{0}\t{1}\t{2}".format(
            post_data[0], post_data[2], answers_len/answers_num)
    else:
        print "{0}\t{1}\t{2}".format(
            post_data[0], post_data[2], answers_len)


for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    post_id, post_type, length = data_mapped

    if post_type == "A":
        if post_data:
            print_data(post_data, answers_num, answers_len)
            post_data = None
            answers_num = 0
            answers_len = 0
        post_data = data_mapped

    if post_type == "B":
        answers_num += 1
        answers_len += float(length)

if post_data:
    print_data(post_data, answers_num, answers_len)
