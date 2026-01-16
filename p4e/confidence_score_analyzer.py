import re
try:
    hand = open('mbox-short.txt')
except FileNotFoundError:
    print("File not found!")
    exit()

numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall("^X-DSAPM-CONFIDENCE: ([0-9.]+)", line)    
    if len(stuff) < 1: 
        continue
    num = float(stuff[0])
    numlist.append(num)

if len(numlist) > 0:
    print("Maximum Confidence:", max(numlist))
    print("Minimum Confidence:", min(numlist))
else:
    print("No matching data.")
