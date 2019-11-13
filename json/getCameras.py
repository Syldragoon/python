from urllib.request import urlopen, Request
import json
import re

serviceUrl = 'https://api.deckchair.com/v1/'
url = serviceUrl + 'cameras'
locationRegex = r'[Pp]aris'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url=url, headers=headers) 

response = urlopen(req);

headers = response.info()
data = response.read()

MyJsonDic = json.loads(data)

if 'success' in MyJsonDic and MyJsonDic['success'] == True:
	print('*** RESULT FOUND ***')
	print('Headers:', headers)
	for cameraData in MyJsonDic['data']:
		if re.search(locationRegex, cameraData["location"]["title"]):
			print ('Camera ID', cameraData["_id"], ' -> ', cameraData["description"], ' (', cameraData["location"]["title"], ")")
else:
	print('*** NO RESULT FOUND! ***')
