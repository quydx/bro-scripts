#curl -XPOST localhost:9200/dga/_search?pretty -d '{"query": {"term": {"domain": "qrwxktojqz.yi.org"}}}'
curl -X GET localhost:9200/dga/_search?pretty -d '{
	"query": {
		"bool": {
			"should": [
				{"match": {"domain": "lykdsevm.mooo.com"}},
				{"match": {"_type": "bobax_dga"}}
			]
		}
	}
}'
#curl -XPOST localhost:9200/dga/_search?pretty -d '{"query": {"term": {"domain": "ns1.backdates0.org"}}}'
#curl -XPOST localhost:9200/dga/_search?pretty -d '{"query": {"term": {"domain": "hmvmgywkvayilcwh.ru", "family":"feodo_dga"}}}'



