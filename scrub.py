"""
This project is responsible for cleaning out noise from a file listing trade information in the format execution time, selling price, and sales volume
*The cleaning process involves converting the data into the right format for evaluation.
*Removing duplicate data points
*Ensuring that price and volume figures are greater than zero
*
Oore Ladipo
"""

#Packages required for completing the imports and cleaning 
#import os 
import sys
from datetime import datetime
from itertools import islice

#Setting up basic logging information
starttime = datetime.now()
print ("Program starts at: ", str(starttime))

#Setting up basic required data structures and variables
thousandlines ={}
counter = 0
batch =1
output =""
linesused = 0
window = 10000
done = False


    
#setting up functions that will be useful later
# function 1 allows me to accept input in x line increments with x being the number specified in window above
def nextlines (filename, linecount):
    return[x.strip() for x in islice(filename, linecount)]
def returntime (starttime, endtime):
    return (endtime - starttime)

#function 2 allows me to clean out the datapoints that have negative prices and negative volumes traded           
def cleanup (datain):
    startclean = datetime.now()
    if datain[1]< 0:
        filenoise.write(str(datain)+'\n')
    elif datain[2]<1:
        filenoise.write(str(datain)+'\n')
    else:
        fileout.write(str(datain)+'\n')
    endclean = datetime.now()
    cleaningtime = endclean - startclean
    #filelog.write(str(cleaningtime)+'\n')
    #filelog.write("This line takes "+str(cleaningtime)+" long to clean")
    return(cleaningtime)

#Setting up both the input and output files (including the timers for both input and output)
fileopentime = datetime.now()
print ("Program opens up the input and output files: ", str(fileopentime))
try:
    fileout = open ("cleandata.txt", 'a') #given concurrency I feel that append might be a better choice than write
    filenoise = open ("noise.txt", 'a')
    filelog = open ('log.txt','a')
    #filesort = open ('sort.txt','a')
    with open(sys.argv[1],'r') as filein:
        inputtime = datetime.now()
        cleantime =datetime.now()
        while done != True:
            if counter == 0:
                lines_window = nextlines(filein, window)
                print("program starts taking input as batches of "+str(window)+": ", str(inputtime))
        
            print("Processing batch number: ",str(batch))
            for line in lines_window:
                try:
                    thousandlines[counter] =line.split(',')
                    thousandlines[counter][0] = datetime.strptime(thousandlines[counter][0], "%Y%m%d:%H:%M:%S.%f")
                    thousandlines[counter][1] = float(thousandlines[counter][1])
                    thousandlines[counter][2] = int(thousandlines[counter][2])
                    cleantime += cleanup(thousandlines[counter])
                    counter +=1
                except:
                    #filenoise.write(output+str(thousandlines[counter])+'\n')
                    pass
            #filesort.write(str(sorted(thousandlines.keys(), key = lambda t:thousandlines[t][0]))+'\n')
            lines_window = nextlines(filein,window)
            batch+=1
            if not lines_window:
                print("You've processed all lines\n")
                filelog.write("The total time spent cleaning the data was "+str(cleantime-inputtime)+'\n')
                filein.close()
                fileout.close()
                filelog.close()
                #filesort.close()
                filenoise.close()
                done = True
                
        
except:
    print("There was an error in the filename argument you passed\n")
    fileout.write("There was an error in the process. Invalid results\n")
    filenoise.write("There was an error in the process. Invalid results\n")
    filein.close()
    fileout.close()
    filelog.close()
    filenoise.close()
    sys.exit(1)


#Starting the process of cleaning the data and writing it to the cleandata file.




# Module for converting data from text string to appropriate format
#* Will check to see if the datetime needs to be converted to time or if it can be compared as string
