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
else:
	exit_line = ""

for line in inputFile:
	if (len(line) < 3): #to avoid \r\n
		pass
	else:
		if (args.output == None):
			#print(line)
			exit_line += line #+ "\r\n"
		else:
			outputFile.write(line)

if (args.output == None):
	print (exit_line)

#close files
inputFile.close()

if (args.output != None):
	outputFile.close()
