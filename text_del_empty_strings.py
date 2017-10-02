#!/usr/bin/python
# removes empty strings 
import sys

if len(sys.argv) < 3:

	print("Usage: {} <file_to_read> <output_file>".format(sys.argv[0]))
	sys.exit(1)

inputFile = open(sys.argv[1])
outputFile = open(sys.argv[2], 'w')

for line in inputFile:
	if (len(line) < 5):
		pass
	else:
		outputFile.write(line)