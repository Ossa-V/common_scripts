#!/usr/bin/python
# removes empty strings 
import sys
import argparse

def withFile(inputFileAddr, outputFileAddr): # If output file defined
	inputFile = open(inputFileAddr)
	outputFile = open(outputFileAddr, 'w')
	for line in inputFile:
		if (len(line) < 3): #to avoid \r\n
			pass
		else:
			outputFile.write(line)
	inputFile.close()
	outputFile.close()
	
def withoutFile(inputFileAddr): # If output not defined
	inputFile = open(inputFileAddr)
	exit_line = ""
	for line in inputFile:
		if (len(line) < 3): #to avoid \r\n
			pass
		else:
			#print(line)
			exit_line += line 
	print(exit_line)
	inputFile.close()

# Main part #

parser = argparse.ArgumentParser(description="Script removes empty strings in input file and writes result to file or console")
parser.add_argument("-i", "--input", type=str, help="Input file to correct")
parser.add_argument("-o", "--output", type=str, help="Write to file (if not specified output to console)")

args = parser.parse_args()


if (args.output != None):
	withFile(args.input, args.output)
else:
	withoutFile(args.input)

