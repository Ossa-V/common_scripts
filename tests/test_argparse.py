#!/usr/bin/python
#import sys
import argparse

'''
The script deletes the data in the first file that are found in the second file.
Is able to work with data in a column and in a string (must be separated by a space).
Prints the data in a column

To Do: Add work without outputfile (output into console via print() )
'''

# Scripts removes entries in file_to_correct

parser = argparse.ArgumentParser(description='Hey, i\'m description, don\'t touch me!')
parser.add_argument("-i", "--input", type=str, help="Input file to correct")
parser.add_argument("-c", "--correct", type=str, help="File with lines will be deleted in input file")
parser.add_argument("-C", type=str, help="Text line for exclude words from input file")
parser.add_argument("-o", "--output", type=str, help="Write to file")
parser.add_argument("-s", "--silent", help="Turn off statistic", action="store_true")

args = parser.parse_args()


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
