import urllib
import json

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_191949.json'

myJson = urllib.urlopen(url).read()

comments = json.loads(myJson)['comments']

count = 0
for comment in comments:
	count += int(comment['count'])

print 'Result:', count