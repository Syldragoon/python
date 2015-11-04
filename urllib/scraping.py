from BeautifulSoup import *
import urllib

myUrl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Keela.html'
linkPos = 18
nbIter = 7

for count in range(nbIter):
    html = urllib.urlopen(myUrl).read()
    soup = BeautifulSoup(html)

    links = soup('a')
    myNewUrl = links[linkPos - 1].get('href', None)
    myNewContent = links[linkPos - 1].contents[0]

    print '--'
    print 'Url:', myUrl
    print 'Third link content:', myNewContent
    print 'Third link url:', myNewUrl
    print '--'

    myUrl = myNewUrl

result = myNewContent
print 'Result:', result
