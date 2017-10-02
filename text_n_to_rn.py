#!/usr/bin/python
import sys


#	Script simply replacing \n with \r\n for better display at windows


if len(sys.argv) < 3:
	print("{} <file1> <output_file>".format(sys.argv[0]))
	print("Script simply replacing \\n with \\r\\n for better view at windows")
	sys.exit(1)

inputFile = open(sys.argv[1])
outputFile = open(sys.argv[2], 'w')

for line in inputFile:
	#outputFile.write(line.replace("\r\n", ", ")) #for network and servers
	#temp2 = tempLine.replace("\r", ", ")
	#outputFile.write(line.replace("\n", " ")) #for main purpose
	outputFile.write(line.replace("\n", "\r\n"))