import os
import csv
Total_Months=[]
Total=[]
Change=[]
Greastest_Increase=[]
Greastest_Decrease=[]
count=0
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile) 
    
    for row in csvreader:
        
        count=count+1
        
    Total_Months.append(count-1)
    print(Total_Months) 
       
