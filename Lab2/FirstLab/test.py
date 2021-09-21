import sys
if len(sys.argv)<2:
    print("enter one file name:- ")
else:
    listofall=[]
    for line in open(sys.argv[1],"r"):
        if line[0].isdigit():
            listofall.append(line)
    for i in range(0,len(listofall)):
        listofall[i]=listofall[i].split(",")
    listofall.sort(key=lambda x:float(x[-2]))
    top20=[]
    bottom40=[]
    for i in range(0,int(len(listofall)*0.4)):
        bottom40.append(listofall[i])
    print("\nthe bottom 40 % of stdents (",len(bottom40),")by marks are :-\n")
    for i in bottom40:
        print(i)
    for i in range(0,int(len(listofall)*0.2)):
        top20.append(listofall[len(listofall)-i-1])
    print("\nthe top 20 % of stdents (",len(top20),")by marks are :-\n")
    for i in top20:
        print(i)