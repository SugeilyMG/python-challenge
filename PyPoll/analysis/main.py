import os
import csv
import sys

candidates=[]
unique_can=set()
votes=[]
names=[]

csvpath = os.path.join("..","Resources", "election_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile) 
    csv_header = next(csvfile)

    for row in csvreader:
        candidates.append(row[2])
        unique_can.add(row[2])

    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:",len(candidates))
    print("-----------------------------------")

    for i in unique_can:
        votes.append(candidates.count(i))
        names.append(i)
        print(i,":",round(candidates.count(i)/len(candidates)*100),"%","(",candidates.count(i),")") 
    max_name=str(names[votes.index(max(votes))])
    print("-----------------------------------")
    print("Winner:",max_name)
    print("-----------------------------------")

    sys.stdout = open("analysis.txt", "w") 
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:",len(candidates))
    print("-----------------------------------")

    for i in unique_can:
        votes.append(candidates.count(i))
        names.append(i)
        print(i,":",round(candidates.count(i)/len(candidates)*100),"%","(",candidates.count(i),")") 
    max_name=str(names[votes.index(max(votes))])
    print("-----------------------------------")
    print("Winner:",max_name)
    print("-----------------------------------")
    sys.stdout.close()
