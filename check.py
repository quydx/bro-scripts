# python domain check 
import re
from pprint import pprint 
import sys
from elasticsearch import Elasticsearch
# family list 
# import MySQLdb

def is_doc(domain, family):
	es = Elasticsearch()
	res = es.search(index = 'dga', body = {
		"query" : {
        	"constant_score" : { 
            	"filter" : {
                	"bool" : {
                    	"must": [
                        	 { "term": { "_type":  "%s" % family}},
                         	 { "term": { "domain": "%s" % domain}}
                     	]
                	}
            	}
        	}
    	}
	})
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



