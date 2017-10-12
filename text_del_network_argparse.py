#!/usr/bin/python
# Searching for lines like 10.0.90.0 and passes it when writing to another file
import argparse

parser = argparse.ArgumentParser(description="Search for strings such as 10.0.90.0, and skips them when writing to another file, so the output file will have all addresses without subnets.")
parser.add_argument("-i", "--input", type=str, help="Input file to correct")
parser.add_argument("-o", "--output", type=str, help="Write to file (if not defined - write to console")

args = parser.parse_args()

if (args.input == None):
    print("[-]\tNo input file specified! Exiting..")
    exit(1)

inputFile = open(args.input)
if (args.output != None):
    try:
        outputFile = open(args.output, 'w')
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        exit(1)
else:
	exit_line = ""


for line in inputFile:
    if line[len(line)-2] == '0':	# checks if there's network like 10.0.0.0 , -2 is \r\n #There can be error if only one special character is used
        pass				# You better add some checks that input isn't text by your own
    else:
        if (args.output != None):
            try:
                outputFile.write(line)
            except IOError as e:
                print("I/O error({0}): {1}".format(e.errno, e.strerror))
                exit(1)
        else:
            exit_line += line

if (args.output == None):
	print(exit_line)

# close opened files
inputFile.close()
if (args.output != None):
	outputFile.close()
