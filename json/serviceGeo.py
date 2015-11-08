import urllib
import json

serviceUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input('Enter address: ')

	url = serviceUrl + urllib.urlencode({'sensor': 'false', 'address': address})
	response = urllib.urlopen(url);

	headers = response.info()
	data = response.read()

	try:
		MyJsonDic = json.loads(str(data))
	except:		
		MyJsonDic = None

	if 'status' in MyJsonDic and MyJsonDic['status'] == 'OK': 
		result = MyJsonDic['results'][0]
		fullAddress = result['formatted_address']
		placeId = result['place_id']
		locLat = result['geometry']['location']['lat']
		locLng = result['geometry']['location']['lng']
		
		print '*** RESULT FOUND ***'
		print 'Headers:', headers
		print 'Full address:', fullAddress
		print 'Place ID:', placeId
		print 'Location:(', locLat, ',', locLng, 	')'
	else:
		print '*** NO RESULT FOUND! ***'