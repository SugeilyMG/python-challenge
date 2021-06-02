import os
import csv
import sys

Profits_=[]
Change=[]
Dates=[]

csvpath = os.path.join("..","Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile) 
    csv_header = next(csvfile)

    for row in csvreader:
        Profits_.append(float(row[1]))
        Dates.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(Dates))
    print("Total:", "${:,.2f}".format(sum(Profits_)))
 
    for i in range(1,len(Profits_)):
            Change.append(Profits_[i]-Profits_[i-1])
            avg_ch=sum(Change)/len(Change)
            max_ch=max(Change)
            min_ch=min(Change)
            date_min=str(Dates[Change.index(min(Change))+1])
            date_max=str(Dates[Change.index(max(Change))+1])

    print("Average Change:", "${:,.2f}".format(round(avg_ch)))
    print("Greatest Increase in Profits:", date_max,"($",max_ch,")")
    print("Greatest Decrease in Profits:", date_min,"($",min_ch,")")

    sys.stdout = open("analysis.txt", "w")  
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(Dates))
    print("Total:", "${:,.2f}".format(sum(Profits_)))
    print("Average Change:", "${:,.2f}".format(round(avg_ch)))
    print("Greatest Increase in Profits:", date_max,"($",max_ch,")")
    print("Greatest Decrease in Profits:", date_min,"($",min_ch,")")
    sys.stdout.close()
        
