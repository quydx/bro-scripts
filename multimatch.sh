curl -X GET localhost:9200/dga/_search?pretty -d '
{
    "query" : {
        "constant_score" : { 
            "filter" : {
                "bool" : {
					"must": [
        				 { "term": { "_type":  "bobax_dga" }},
       					 { "term": { "domain": "csukibyyt.mooo.com"}}
     				 ]
                }
            }
        }
    }
}'
