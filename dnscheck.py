from pprint import pprint 
import os
import re
from check import is_doc
import time 


# function read line of file in real-time
def follow(thefile):
	thefile.seek(0, 2)
	while True:
		line = thefile.readline()	
		if not line:
			time.sleep(0.1)
			continue
		yield line	
# return family of a domain 
def getfamily(domain):
	# read all line of list-dga.txt to array list_dga
	with open('list-dga.txt', 'r') as file_content:
		list_dga = eval(file_content.read())
	i = 0 
	family = []
	for dga in list_dga:
		if 'regex' in dga:
			if re.match( r'^%s' % dga['regex'], domain ):
				family.append(dga['name'])
		i+=1
	return family
# function get file has $name in filename in $path
# return (str) name
def find(name, path):
	for files in os.listdir(path):
		if (re.match(r'^{}'.format(name), files) != None):
			return files
### __main__
path = '/usr/local/bro/logs/current/'
file_name = find('dns', path)
f = open(path + file_name, "r")
all_lines = follow(f)
for line in all_lines:
	if '#' not in line:
		arr = line.split('\t')
		if len(arr) <= 8:
			continue
		family = getfamily(arr[9])
		if (len(family) == 0): 
			continue
		if is_doc(arr[9], getfamily(arr[9])[0]) != False:
			print(arr[9])
			print(family)
			logfile = open('/var/log/dga/dga-dns.log', "a+")
			logfile.write("%s\n" % line)
			logfile.close()
"""
	print("DGA domain count : %d" %dga)
	print("All domain count : %d" %_all)
	print("Rate: {} %".format((dga/_all*100)) )
"""
1505209244.121602	CxI4la44O1QYKQZldc	192.168.142.113	38825	8.8.8.8	53	udp	64995	0.034276	ghcxncadnj.dyndns.org	1	C_INTERNET	12	PTR	3	NXDOMAIN	F	F	T	T	0	223.0-24.193.212.125.in-addr.arpa	72281.000000	F
