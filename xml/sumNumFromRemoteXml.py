import urllib
import xml.etree.ElementTree as ET

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_191945.xml'

xml = urllib.urlopen(url).read()
xmlTree = ET.fromstring(xml)

countTags = xmlTree.findall('.//count')

count = 0
for countTag in countTags:
    count += int(countTag.text)
print 'Sum of numbers:', count
