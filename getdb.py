#import pycurl
#from  BeautifulSoup import BeautifulSoup as BS
from pprint import pprint
import re
from io import StringIO
from io import BytesIO

filename = 'response.txt'
url = 'https://dgarchive.caad.fkie.fraunhofer.de/site/families.html'
user = 'do'
pwd = 'hyuticahuberarlentitus'
"""
with open('response.txt','wb') as f:
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEDATA, f)
	c.setopt(pycurl.USERPWD, '%s:%s'%(user, pwd))
	c.perform()
	c.close()
"""
list_name = list()
list_regex = list()
with open(filename) as f:
	content = f.readlines()
	print(len(content))
	for i in range(len(content)):
		tags = str(content[i]).replace('\n', '').replace('\t','')
		if '#' in tags:
			name = re.match(r'^(.*)<td><a href="#(.*)">(.*)</a></td>(.*)$', tags)
			if name:
				print(name.group(2))
				list_name.append(name.group(2))
		if '$' in tags:
			regex = re.match(r'^(.*)<strong>(.*\$)</strong>(.*)$', tags)
			list_regex.append(regex.group(2))
pprint(list_regex)
print(len(list_regex))
