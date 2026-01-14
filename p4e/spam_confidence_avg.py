
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    k=float(line[19:])
    tot=tot+k
print("Average spam confidence:",tot/count) 
