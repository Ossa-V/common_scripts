#!/usr/bin/python
import argparse

def withFile (inputFileAddr, outputFileAddr):
	inputFile = open(inputFileAddr)
	outputFile = open(outputFileAddr, 'w')
	domains = []

	for line in inputFile: # We assume that one line = one word
		if line.lower().replace("\n", "") not in domains:
			domains.append(line.lower().replace("\n", ""))

	for element in domains:
		if (len(element) > 0):
			outputFile.write(element + "\r\n")

	inputFile.close()
	outputFile.close()
	
def withoutFile (inputFileAddr):
	inputFile = open(inputFileAddr)	
	domains = []

	for line in inputFile: # We assume that one line = one word
		if line.lower().replace("\n", "") not in domains:
			domains.append(line.lower().replace("\n", ""))
	
	exit_line = "" #temp line for output
	for element in domains:
		if (len(element) > 0): #escaping empty strings
			#print ("Element \"{}\" is passed validation with len \"{}\"!".format(element, len(element)))
			if element != domains[-1]:
				exit_line += element + "\n"
			else:
				exit_line += element
	
	print (exit_line)
	inputFile.close()

# Main part #

parser = argparse.ArgumentParser(description="Removes uppercase duplicates, transform all text to lowercase")
parser.add_argument("-i", "--input", type=str, help="Input file to correct")
parser.add_argument("-o", "--output", type=str, help="Write to file (if empty - write to console")

args = parser.parse_args()

if (args.output != None):
    withFile(args.input, args.output)
else:
	withoutFile(args.input)
