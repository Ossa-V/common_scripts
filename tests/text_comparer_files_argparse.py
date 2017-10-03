#!/usr/bin/python
import sys
import argparse

'''
The script deletes the data in the first file that are found in the second file.
Is able to work with data in a column and in a string (must be separated by a space).
Prints the data in a column

To Do: Add work without outputfile (output into console via print() )
'''

#Scripts removes entries in file_to_correct

# Проблема:
# Скрипт работает обязательно с файлами. И обязательно с тремя.
# Соответственно задача - обеспечить возможность для работы с текстовыми данными, вне файла.
# Обеспечить следующие варианты:
# 1) Файл - фраза - вывод в консоль
# 2) Файл - фраза - вывод в файл
# 3) Файл - файл  - вывод в консоль
# 4) Файл - файл  - вывод в файл
# Первый элемент будет файл, т.к. предполагается, что в нем большой объем данных. 
# Подумать как можно организовать передачу данных по трубе.
# Добавить отключение отладочной информации в случае вывода в консоль. Либо перенесети её в верхнюю часть (всю).

def parse_args():
	parser = argparse.ArgumentParser(description='Hey, i\'m description, don\'t touch me!')
	parser.add_argument("-i", "--input", help="Input file to correct")
	parser.add_argument("-c", "--correct", help="File with lines will be deleted in input file")
	parser.add_argument("-o", "--output", help="Write to file")


if len(sys.argv) < 4:
	print("{} <file_to_correct> <comparing_file> <output_file>".format(sys.argv[0]))
	print("The script deletes the data in the first file that are found in the second file.\n		
		Is able to work with data in a column and in a string (must be separated by a space).\n
		Prints the data in a column.")
	sys.exit(1)

inputFile = open(sys.argv[1])
comparingFile = open(sys.argv[2])
outputFile = open(sys.argv[3], 'w')

inputText = (inputFile.read()).split()
compare = (comparingFile.read()).split()
print("In input file {} objects".format(len(inputText)))
print("In compare file {} objects".format(len(compare)))
counter = 0
for inputItem in inputText:
	if inputItem not in compare:
		outputFile.write(inputItem+"\n")
		counter += 1
	else:
		pass

print("In output file {} objects".format(counter))