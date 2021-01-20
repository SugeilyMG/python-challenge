import os
import csv
Total_Months=[]
New_List=[]
Change=[]
Greastest_Increase=[]
Greastest_Decrease=[]
count=0
total=0
avg=0
diff=0

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile) 
    csv_header = next(csvfile)
    for row in csvreader:
        New_List.append(int(row[1]))
        total += int(row[1])
        count = count+1
        avg=total/count    
    Total_Months.append(count)
    print(Total_Months) 
    print(total)
    print(New_List)
    for i in New_List:
        prev=New_List[0]
        curr=New_List[1]
        if i<len(New_List):
            diff += float(curr - prev)
            Change.append(diff)
            prev = curr
            curr = i
    print(Change)
