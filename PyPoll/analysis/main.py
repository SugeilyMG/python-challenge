import os
import csv
import sys

candidates=set()
csvpath = os.path.join("..","Resources", "election_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile) 
    csv_header = next(csvfile)

    for row in csvreader:
        candidates.add(row[2])
        