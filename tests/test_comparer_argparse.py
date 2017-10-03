#!/usr/bin/python
#import sys
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
parser.add_argument("-s", "--silent", help="Turn off statistic", action="store_true")

args = parser.parse_args()

if (args.input == None):
    print("No input file specified! Exiting..")
    exit(1)
else:
    inputText = (open(args.input).read()).split() # Read input file and split text into list
    compareText = ""
    if (args.correct != None): #Now we gonna try to read compare text or string
        compareText = (open(args.correct).read().split()) # Read correct file and split text into list. # To Do: Add exception here, if we couldn't open file.
    elif (args.C != None):
        compareText = args.C
    else:
        print ("Couldn't read correct file or string. Exiting...")
        exit(1)

    if (args.silent == None):
        print("[*]\tIn input file {} objects".format(len(inputText)))
        print("[*]\tIn compare file {} objects".format(len(compareText)))

    counter = 0
    for inputItem in inputText:
        if inputItem not in compareText:
            if (args.output != None): #if item not in compare we write it to the output
                open(args.output, 'w').write(inputItem + "\n") #Add Exception
            else:
                print(inputItem)
        else:
            pass #if item in compare list we skip it

    if (args.silent == None):
        print("[*]\tIn output file {} objects".format(counter))
'''
# Checks that it's working
if (args.silent):
    print("[*]\tSilent mode specified, turning debug messages off..")

if (args.input == None):
    if args.silent != True:
        print("[-]\tNo input file defined, exiting...")

    exit(1)

if (args.correct == None and args.C == None):
    if args.silent != True:
        print("[-]\tNo correct line or file specified, exiting...")

    exit(1)

if (args.output == None):
    if args.silent != True:
        print("[*]\tNo output file defined, writting to console...")

print("\nAll is ok!")

print("\nInput: {}\nCorrect: {}\nOutput: {}\nSilent: {}".format(args.input, args.correct, args.output, args.silent))
'''