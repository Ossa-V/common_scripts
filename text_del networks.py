#!/usr/bin/python
import sys


# Searching for lines like 10.0.90.0 and passes it when writing to another file


if len(sys.argv) < 3:
	print("Usage: {} <file_to_read> <output_file>".format(sys.argv[0]))
	sys.exit(1)

inputFile = open(sys.argv[1])
outputFile = open(sys.argv[2], 'w')

for line in inputFile:
	if line[len(line)-2] == '0':
		pass
	else:
		outputFile.write(line)