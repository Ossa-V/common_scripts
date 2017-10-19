#!/usr/bin/python
# -*- coding: utf-8 -*- 
#we got some problems with ecndoing, need to solve (when we write to the file or using pipe we got error)
import lxml.html as html

# http://www.edudic.ru/fam/1/
for item in range(1,15151):
	page = html.parse('http://www.edudic.ru/fam/{}/'.format(item))
	print (page.find(".//title").text[0:-60])
