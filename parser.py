from bs4 import BeautifulSoup
from pprint import pprint 

list_dga = []
with open('response.html') as file_content:	
	content = file_content.read()
soup = BeautifulSoup(content, 'html.parser' )
all_h3 = soup.find_all('h3')
all_table = soup.find_all('table')
leng = len(all_table)
if (leng == len(all_table)): 
	print "leng is equal %d " % leng
i = 0;
for table in all_table:
	ob = {}
	name = all_h3[i].get('id').replace('-details', '')
	ob['name'] = name
	strongs = table.find_all('strong')
	if (strongs):
		if ('$' in str(strongs[0].get_text())):
			ob['regex'] = strongs[0].get_text()
	i+=1
	list_dga.append(ob)
f = open('list-dga.txt', 'w+')
print >> f, list_dga
f.close()
