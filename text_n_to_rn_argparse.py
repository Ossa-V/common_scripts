#!/usr/bin/python
import sys
import argparse

parser = argparse.ArgumentParser(description="Script simply replacing \\n with \\r\\n for better view at windows or backwards")
parser.add_argument("-i", "--input", type=str, help="Input file to correct")
parser.add_argument("-o", "--output", type=str, help="Write to file")
parser.add_argument("-m", "--mode", type =int, help="-m 1 - replace \\r\\n with \\n\n -m 2 replace \\n with \\r\\n", default=False, action="store_true")

args = parser.parse_args()

inputFile = open(args.input)
outputFile = open(args.output, 'w')
if args.mode == 1:
	for line in inputFile:
		outputFile.write(line.replace("\r\n", "\n"))
elif args.mode == 2:
	for line in inputFile:

		outputFile.write(line.replace("\n", "\r\n"))
else:
	print ("Bad mode (1 or 2). Exiting...")
	sys.exit(1)

inputFile.close()
outputFile.close()
