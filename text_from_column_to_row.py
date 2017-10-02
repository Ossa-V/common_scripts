#!/usr/bin/python
#The script replaces the hyphenation so that the data is written in one line.


import sys

if len(sys.argv) < 3:
	print("{} <file1> <output_file>".format(sys.argv[0]))
	print(sys.argv)
	sys.exit(1)

inputFile = open(sys.argv[1])
outputFile = open(sys.argv[2], 'w')

replacer = ", "

for line in inputFile:
	#outputFile.write(line.replace("\r\n", replacer)) #for network and servers
	#temp2 = tempLine.replace("\r", replacer)
	outputFile.write(line.replace("\n", replacer)) #for main purpose