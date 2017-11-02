#!/usr/bin/python
import sys


'''
The script deletes the data in the first file that are found in the second file.
Is able to work with data in a column and in a string (must be separated by a space).
Prints the data in a column

To Do: Add work without outputfile (output into console via print() )
'''


#Scripts removes entries in
if len(sys.argv) < 4:
	print("{} <file_to_correct> <comparing_file> <output_file>".format(sys.argv[0]))
	print("The script deletes the data in the first file that are found in the second file.\n
		Is able to work with data in a column and in a string (must be separated by a space).\n
		Prints the data in a column.")
	sys.exit(1)

inputFile = open(sys.argv[1])
comparingFile = open(sys.argv[2])
outputFile = open(sys.argv[3], 'w')

input = (inputFile.read()).split()
compare = (comparingFile.read()).split()
print("In input file {} objects".format(len(input)))
print("In compare file {} objects".format(len(compare)))
counter = 0
for inputItem in input:
	if inputItem not in compare:
		outputFile.write(inputItem+"\n")
		counter += 1
	else:
		pass

print("In output file {} objects".format(counter))

# close opened files
inputFile.close()
comparingFile.close()
outputFile.close()
