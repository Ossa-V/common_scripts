#!/usr/bin/python
# Searching for lines like 10.0.90.0 and passes it when writing to another file
import argparse

parser = argparse.ArgumentParser(description="Script simply replacing \\n with \\r\\n for better view at windows or backwards")
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

for line in inputFile:
    if line[len(line)-2] == '0': # checks if there's network like 10.0.0.0 , -2 is \r\n
        pass
    else:
        if (args.output != None):
            try:
                outputFile.write(line)
            except IOError as e:
                print("I/O error({0}): {1}".format(e.errno, e.strerror))
                exit(1)
        else:
            print(line)

# close opened files
inputFile.close()
outputFile.close()
