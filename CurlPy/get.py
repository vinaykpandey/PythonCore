#/usr/bin/python
'''
curl request
resposne:
{"results": [{"alternatives": [{"confidence": 0.7269427, "transcript": "hello Pandey Ji how are you doing"}]}]


 json.dumps({'apple': 'cat', 'banana':'dog', 'pear':'fish'})
'{"pear": "fish", "apple": "cat", "banana": "dog"}'

json.loads( encoded_str )
'''
import requests
import json
from StringIO import StringIO

def curl_get_request():
    url = "http://localhost:8888/curl_get.php"
    response = requests.post(url,data={'key1':'value1', 'key2':'value2'})
    jString = response.content # string
    jload =  json.loads(jString) # dictionary
    return jload

if __name__ == "__main__":

	dData = curl_get_request()
        print dData
        #print dData['name'];

