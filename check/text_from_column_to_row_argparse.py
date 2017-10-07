#!/usr/bin/python
#The script replaces the hyphenation so that the data is written in one line.
import argparse

parser = argparse.ArgumentParser(description="Script simply replacing \\n with \\r\\n for better view at windows or backwards")
parser.add_argument("-i", "--input", type=str, help="Input file to correct")
parser.add_argument("-o", "--output", type=str, help="Write to file (if empty - write to console")
parser.add_argument("-r", "--replacer", type =str, default=" ", help="string to replace \\n (default space)")

args = parser.parse_args()

inputFile = open(args.input)
if (args.output != None):
    try:
        outputFile = open(args.output, 'w')
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        exit(1)


if (args.output != None):
    try:
        outputFile.write(inputFile.read().replace("\n", args.replacer))
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        exit(1)
else:
    print(inputFile.read().replace("\n", args.replacer)) #read full file and replace \n
	
# close opened files
inputFile.close()
outputFile.close()
