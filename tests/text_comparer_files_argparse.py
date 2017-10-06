#!/usr/bin/python
import argparse

'''
The script deletes the data in the first file that are found in the second file.
Is able to work with data in a column and in a string (must be separated by a space).
Prints the data in a column
To Do: Add work without outputfile (output into console via print() )
'''

# Scripts removes entries in inputfile which was found in correct file

parser = argparse.ArgumentParser(description='Hey, i\'m description, don\'t touch me!')
parser.add_argument("-i", "--input", type=str, help="Input file to correct")
parser.add_argument("-c", "--correct", type=str, help="File with lines will be deleted in input file")
parser.add_argument("-C", type=str, help="Text line for exclude words from input file") #dunno how it's gonna work with "c" arg and "C".
parser.add_argument("-o", "--output", type=str, help="Write to file")
parser.add_argument("-s", "--silent", help="Turn off statistic", default=False, action="store_true")

args = parser.parse_args()

if (args.input == None):
    print("[-]\tNo input file specified! Exiting..")
    exit(1)
else:
    inputText = (open(args.input).read()).split() # Read input file and split text into list

    compareText = ""
    if (args.correct != None): #Now we gonna try to read compare text or string
        compareText = (open(args.correct).read().split()) # Read correct file and split text into list. # To Do: Add exception here, if we couldn't open file.
    elif (args.C != None):
        compareText = args.C
    else:
        print ("[-]\tCouldn't read correct file or string. Exiting...")
        exit(1)

    if (args.silent == False):
        print("[*]\tIn input file {} objects".format(len(inputText)))
        print("[*]\tIn compare file {} objects".format(len(compareText)))

    #Debug
    #print ("Input Text:\n{}".format(inputText))
    #print ("CompareText:\n{}".format(compareText))

    outputFile = open(args.output, 'w')
    counter = 0
    for inputItem in inputText:
        if inputItem not in compareText:
            if (args.output != None): #if item not in compare we write it to the output
        #print("Output: {}".format(inputItem)) Debug
                outputFile.write(inputItem + "\n") #Add Exception if we couldn't open file
            else:
                print(inputItem)
        else:
        #Debug
        #print ("Input {} found in {}!".format(inputItem, compareText))
            pass #if item in compare list we skip it

    if (args.silent == False):
        print("[*]\tIn output file {} objects".format(counter))

    outputFile.close()
