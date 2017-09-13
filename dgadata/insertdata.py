import os
import re
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime

os.system('curl -XDELETE localhost:9200/dga')
es = Elasticsearch()
file_names = [f for f in os.listdir() if os.path.isfile(f) and f.split('.')[1] == 'csv' ]
for file_name in file_names:
	doc_array =[]
	lines = [line.rstrip('\n') for line in open(file_name)]
	for i in range(len(lines)):
		str1 = '['+ lines[i]+ ']'
		array_data = eval(str1)
		leng = len(array_data)
		for j in range(1, leng -1):
			array_data.pop(1)
		array_data[1] = array_data[1].split('_dga', 1)[0] + '_dga'
		keys = ['domain', 'family']
		data = zip(keys, array_data)
		json_data = dict(data)
		data_type = re.search(r'^(.*)(\.{1,1})(.*)$', file_name)
		action = {
			"_index": "dga",
			"_type": data_type.group(1),
			"_id": i,
			"_source": json_data
		}
		doc_array.append(action)
	print(len(doc_array))
	helpers.bulk(es, doc_array)

es.indices.refresh(index ='dga')
res = es.search(index = 'dga', body = {"query": {"match_all": {}}})
print("Got %d hits" %res['hits']['total'])
