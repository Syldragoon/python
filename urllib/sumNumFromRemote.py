import urllib
from BeautifulSoup import *

myUrl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_191948.html'

myData = urllib.urlopen(myUrl).read()

soup = BeautifulSoup(myData)
spans = soup('span')

count = 0
for span in spans:
  count += int(span.contents[0])

print 'Sum of numbers:', count
