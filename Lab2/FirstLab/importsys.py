import sys
if len(sys.argv)<2:
    print("not a valid argument")
else:
    f = open(sys.argv[1],"r")
   
    content = f.read()
    
    f.close()
    print(content)
    
    

    