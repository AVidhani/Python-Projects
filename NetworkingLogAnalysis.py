import sys, string, os

try:
    in_file = open("log.txt","r")
except FileNotFoundError:
    print("File not Found " + "expinput.txt")
    raise
except IOerror:
    print("could not open the file " + "expinput.txt")
else:

    for line in in_file:
        if "GET" in line:
            parts = line.split("GET")
            subParts1= parts[1].split()
            if "html" in subParts1[0]:
                subParts0= parts[0].split()
                date=subParts0[0]
                lName=list(subParts1[0]) #stores the log file name
                fname=''.join(lName[1:]) #stores the filepath
                host1=subParts0[3]
                host2=subParts1[4]
                print(str(date) + "|" + str(fname) + "|" + str(host1) + "|" + str(host2))
