import sys
import csv
j=0

def verify(n):
    if n[30]=="1":
        return True
    




if len(sys.argv)<2:
    print("not a valid argument")
else:

    with open('../marks.csv',"r") as f:
        csv_reader=csv.reader(f)
 
        
    
        for i in csv_reader :
           if(i[0].isdigit()):
                if i[2]=="NA":
                  i[2]="0" 
                if i[3]=="NA":
                  i[3]="0"    
                if i[4]=="NA":
                  i[4]="0" 
                if i[5]=="NA":
                  i[5]="0" 
                if i[1]=="NA":
                  i[1]="0"         


               
                f=float(i[1])+float(i[2])+float(i[3])+float(i[4])+float(i[5])
                i.append(str(f))
                print(i)

               
             
                          
            
            
      

        
      