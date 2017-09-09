from pprint import pprint 
import os
import re
from check import is_doc

with open('list-dga.txt', 'r') as file_content:
	list_dga = eval(file_content.read())
		
def getfamily(domain):
	i = 0 
	family = []
	for dga in list_dga:
		if 'regex' in dga:
			if re.match( r'^%s' % dga['regex'], domain ):
				family.append(dga['name'])
		i+=1
	return family

path = '/usr/local/bro/logs/current/'
def find(name, path):
	for files in os.listdir(path):
		if (re.match(r'^{}'.format(name), files) != None):
			return files
file_name = find('dns', path)

with open(path + file_name) as f:
	content = f.readlines()
	_all = len(content)
	dga = 0
	for i in range(len(content)):
		if '#' not in content[i]:
			arr = content[i].split('\t')
			family = getfamily(arr[9])
			if (len(family) == 0): 
				continue
			if is_doc(arr[9]) != False:
				print(arr[9])
				print(family)
				dga+=1
	print("DGA domain count : %d" %dga)
	print("All domain count : %d" %_all)
	print("Rate: {} %".format((dga/_all*100)) )
