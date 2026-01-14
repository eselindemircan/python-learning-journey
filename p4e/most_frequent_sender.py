
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)    
bignum=dict()
for line in handle:
    words=line.split()
    if len(words)<1 or words[0] !="From":
        continue
    sender=words[1]    
    bignum[sender]=bignum.get(sender,0)+1
bigcount=None
bigsender=None
for sender,count in bignum.items():
     if bigcount is None or count>bigcount:
           bigcount=count
           bigsender=sender
print(bigsender,bigcount)
   
#bir dosyadaki en cok mail atan ve attigi mail sayisi
