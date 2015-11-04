import re

fileName = 'regex_sum_191943.txt'

with open(fileName, 'r') as f:
  read_data = f.read()

numList = re.findall('[0-9]+', read_data)

count = 0
for num in numList:
  count += int(num)

print 'sum of numbers computed from file', fileName, ':', str(count)
