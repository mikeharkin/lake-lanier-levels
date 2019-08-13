import csv
import urllib.request

import pandas as pd

current_year = 'http://water.sam.usace.army.mil/gage/acf/prob1.txt'

# with urllib.request.urlopen(current_year) as f:
#     line = f.readline()
#     while line:
#         line_list = line.strip().decode().split()
#         print(line_list)
#         line = f.readline()

with urllib.request.urlopen(current_year) as f:
	months = f.readlines()[3]

	print(months)

	lines = f.readlines()[5:36]#.strip().decode().split()
	for line in lines:
		print(line.split())