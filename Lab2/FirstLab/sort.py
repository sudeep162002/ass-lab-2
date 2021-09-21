import sys
import csv


def verify(n):
    if n[30]=="1":
        return True
    
counter=0


if len(sys.argv)<2:
    print("not a valid argument")
else:

    with open('marks.csv',"r") as f:
        csv_reader=csv.reader(f)
       
        
    
        for i in csv_reader:
           print(i)


print(len(result))