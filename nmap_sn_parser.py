#!/usr/bin/python
#This script parses nmap output of this command:
#nmap -sn 10.0.0.0-10.0.0.255 (or another range)
#Which contains string "Nmap report for ****" so we can use this line to detect active hosts.
#At the output of this script, we get a list of IP addresses active at the time of scanning. 
#For the correct display in Windows, replace \n with \r\n
import sys

if len(sys.argv) < 3:
	print("{} <file_to_be_parsed> <output_file>".format(sys.argv[0]))
	sys.exit(1)

inputFile = open(sys.argv[1])
outputFile = open(sys.argv[2], 'w')

for line in inputFile:
	if line[0] == 'N':
		temp = line.split()
		ip = temp[4]
		outputFile.write(ip+'\n') #Change \n here with \r\n for Windows
	else:
		pass