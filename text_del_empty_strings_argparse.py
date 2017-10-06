#!/usr/bin/python
# removes empty strings 
import sys
import argparse

parser = argparse.ArgumentParser(description="Script removes empty strings in input file and writes result to file or console")
parser.add_argument("-i", "--input", type=str, help="Input file to correct")
parser.add_argument("-o", "--output", type=str, help="Write to file (if not specified output to console)")

args = parser.parse_args()

inputFile = open(args.input)

if (args.output != None):
	outputFile = open(args.output, 'w')

for line in inputFile:
	if (len(line) < 2):
		pass
	else:
		outputFile.write(line)

#close files
inputFile.close()
if (args.output != None):
	outputFile.close()
