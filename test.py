#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from tkinter import *

tree = ET.parse('country_data.xml')
root = tree.getroot()

print(root)

print(root.tag)

parser = ET.XMLPullParser(['start', 'end'])

parser.feed('<mytag>sometext')

list(parser.read_events())

parser.feed(' more text</mytag>')

for event, elem in parser.read_events():
     print(event)
     print(elem.tag, 'text=', elem.text)


for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for country in root.findall('country'):
     rank = country.find('rank').text
     name = country.get('name')
     print(name, rank)

#Change XML
for rank in root.iter('rank'):
     new_rank = int(rank.text) + 1
     rank.text = str(new_rank)
     rank.set('updated', 'yes')


tree.write('output.xml')

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
         root.remove(country)


tree.write('output.xml')
