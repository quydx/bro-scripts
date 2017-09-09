# python domain check 
import re
from pprint import pprint 
import sys
from elasticsearch import Elasticsearch
# family list 
# import MySQLdb
def get_family(domain):
	for family in dm_regex:
		if re.match(r'%s' % family[1], domain):
			return family[0]
	return False
def is_doc(domain):
	es = Elasticsearch()
	res = es.search(index = 'dga', body = {"query": {"term": {"0": domain}}})
	if res['hits']['total'] > 0:
		return res
	else:
		return False

def is_in_database(domain):
	db = MySQLdb.connect("localhost", "root", "123456", "dga")
	cursor = db.cursor()
	table = get_family(domain)
	if (table != False ):
		sql_query = "SELECT domain FROM {} WHERE domain = '{}'".format(table, domain)
		cursor.execute(sql_query)
		res = cursor.fetchall()
		if (res.count() >= 0):
			return True
			db.close()
		else:
			return False
			db.close()
	
#domain = sys.argv[1]



