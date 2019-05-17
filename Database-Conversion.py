#expinput.txt file has data of employees, their yearly or monthly income and number of hours. However, each data point is on a separate line in the file.
#this program applies an algorithm based on the data structure inside the file which accurately extracts the required fields and aggregates the amount and hours
#for each employee into a single record, which is then saved into the expoutput.csv file. Once, in a .csv format, we can use the prepared data for analysis

import sys, string

try:
    in_file = open("expinput.txt","r")
except FileNotFoundError:
    print("File not Found " + "expinput.txt")
    raise
except IOerror:
    print("could not open the file " + "expinput.txt")
else:
    out_file = open("expoutput.csv", "w")#the option "w" will create a new file or overwrite the existing one. To append use option "a"
    custID = 0
    count = 0 #flag to prevent writing the record to output file, when just the first line from the input file is being read
    for line in in_file.readlines():
        parts = line.split(",")
        if custID != parts[0]:
            if count > 0:
                out_file.write(custID + ", " + name + " " + Sname + ", " + str(amt) + ", " + str(hours)+"\n")#the variables are initiated below but would not cause error because the if condition will not be executed when count=0
            else:
                count += 1
                
            #first occurence of new custID will contain only the name fields .Amount and hours will be in the following lines which is handled in the else condition.
            name = parts[2]
            Sname = parts[1]
            amt = 0
            hours = 0

        else:
            #when custID is repeated in next line, the following if condition extracts amount and hours based on presence of Y or M characters in the line
            if parts[2] == "Y" or parts[2] == "M":
                amt += float(parts[3])
            else:
                hours += int(parts[2])
        custID=parts[0]#save the customerID from file in this variable to compare with the customer ID in the next line when the program iterates through the input file
        
            

    out_file.write(custID + ", " + name + " " + Sname + ", " + str(amt) + ", " + str(hours)+"\n")#save the last record to the output file
    out_file.close()
    in_file.close()
