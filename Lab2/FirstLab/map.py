import sys
import csv
sumSel=0
def selCount(selStudent):
    if selStudent[6]=='1':
        return 1






f= open(sys.argv[1],"r")
reader=csv.reader(f)
selectedCount=map(selCount,reader)
for finalCount in list(selectedCount):
    if finalCount==1:
        sumSel+=1
        print(finalCount) 
       




    