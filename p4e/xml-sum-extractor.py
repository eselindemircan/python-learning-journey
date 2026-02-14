import urllib.request
import xml.etree.ElementTree as ET

url =  'http://py4e-data.dr-chuck.net/comments_2346298.xml' 

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')


tree = ET.fromstring(data)


counts = tree.findall('.//count')

nums = list()

for item in counts:
    
    nums.append(int(item.text))


print('Count:', len(nums))
print('Sum:', sum(nums))
