#!/usr/bin/python
# -*- coding: utf-8 -*-
# Works only with file output
# With progressbar (uses progressbar lib)

import lxml.html as html
import argparse
from progressbar import ProgressBar, Bar, ETA, Percentage

#def progress(counter): # Status report
#	if counter % 5 == 0:
#		print ("{} objects done...\r".format(counter))

parser = argparse.ArgumentParser(description="Parses title of pages (remove text[0:-60] for full title)")
parser.add_argument("-o", "--output", type=str, help="Write to file (if empty - write to console")
args = parser.parse_args()
# is file specified?
if args.output != None:
	outputFile = open(args.output, 'w')
else:
	print("Output file not specified")

#progress bar init
pbar_widgets = ['Progress: ', Percentage(), ' ', Bar(), ' ', ETA(), ' ']
pbar = ProgressBar(widgets=pbar_widgets)

# http://www.edudic.ru/fam/1/ # last 15181
lastitem = 500
for item in pbar(range(1,lastitem + 1)):
	page = html.parse('http://www.edudic.ru/fam/{}/'.format(item))
	outputFile.write(page.find(".//title").text[0:-60].encode('utf-8')+"\r\n")
	#progress(item)

print ("FIN")
if args.output != None:
	outputFile.close()
