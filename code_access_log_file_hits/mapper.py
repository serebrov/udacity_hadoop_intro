#!/usr/bin/python

# Web server log file from a public relations company whose clients
# were DVD distributors
# Format:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
# 10.211.47.159 - - [03/Jan/2010:18:15:24 -0800] "GET /assets/js/the-associates.js HTTP/1.1" 304 -
# %h %l %u %t \"%r\" %>s %b
# Where:
#  %h is the IP address of the client
#  %l is identity of the client, or "-" if it's unavailable
#  %u is username of the client, or "-" if it's unavailable
#  %t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
#  %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
#  %>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
#  %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.
#
# For this task we need the number of hits for each file,
# key = file name, value = 1 (1 hit for each log record)

import sys
import re

regex = '([(\d\.)]+) ([^\s]+) ([^\s]+) \[(.*?)\] "(\w+) ([^\s]+) ([^\s]+)" (\d+) ([^\s]+)'
r = re.compile(regex)

for line in sys.stdin:
    matches = r.match(line)
    if matches:
        print "{0}\t{1}".format(matches.groups()[5], 1)
    else:
        print 'No matches: %s' % line
