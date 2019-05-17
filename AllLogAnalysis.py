import sys, string, os

path = 'AllLogs/'
listing = os.listdir(path)
for infile in listing:

    in_file = open(path+infile,"r")
    print("current file is: " + infile)
    for line in in_file:
        if "GET /index.html" in line:
            parts = line.split("GET")
            subParts1= parts[1].split()
            #if "html" in subParts1[0]:
            subParts0= parts[0].split()
            date=subParts0[0]
            lName=list(subParts1[0])
            fname=''.join(lName[1:])
            host1=subParts0[3]
            host2=subParts1[4]
            print(str(date) + "|" + str(fname) + "|" + str(host1) + "|" + str(host2))
    in_file.close()