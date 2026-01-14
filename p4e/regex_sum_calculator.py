import re
ink = input("Enter a file: ")
handle=open(ink)
counts=list()
sum=0
for line in handle:
    line=line.rstrip()
    num=re.findall("[0-9]+", line)
    for n in num:
        numi=int(n)
        counts.append(numi)
        sum=sum+numi
print("Sum: ", sum)
