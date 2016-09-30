#!/usr/bin/env python
# Parse the transports files (json) into a csv file 
# Author: Angel J. Lopez @ UGent
# Date: Sep 12, 2016
# 
# Usage:
#
# ./parse-to-csv.py input-file > output-file
# 
# or 
#
# cat input-file | ./parse-to-csv.py > output-file


import sys
import json
import csv


# read the file (parameter) or the standard input
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin    
# write on the standard output
f_w = csv.writer(sys.stdout)

# waypoints is the default option
op = sys.argv[2] if len(sys.argv)>2 else 'waypoints'
datatype = op if op=='augmented_trajectory' else 'waypoints' #  'waypoints'

count=0   # line reference
header=0  # header flag
for line in f:
	data = json.loads(line)
	pt_cnt=0  # location count
	count +=1 
	for item in data[datatype]:
		pt_cnt+=1	
		row_value = item 
		row_value['atomid'] = data['atomid']
		row_value['userid'] = data['userid']
		row_value['starttime'] = data['startedAt']
		row_value['stoptime'] = data['endedAt']
		row_value['mode'] = data['label']
		row_value['loc_seq'] = pt_cnt
		row_value['segment_seq'] = count

		if header==0:
 			f_w.writerow(row_value.keys())
 			header=1
		f_w.writerow(row_value.values())