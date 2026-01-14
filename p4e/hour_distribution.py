name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    line=line.rstrip()
    if len(line)<1:
        continue
    if not line.startswith("From"):
        continue
    words=line.split()
    if len(words)<6:
        continue
    time=words[5]
    hours_list = time.split(":")
    hour=hours_list[0]
    counts[hour] = counts.get(hour, 0) + 1
lst=sorted(counts.items())
for k, v in lst:
    print(k, v)
