import re


neg=set()

for line in open("common_negative_words.txt","r"):
    neg.add(line.strip())


file=[]
for line in open("sysmgr-test-1.txt","r"):
    file.append(line)


index=set()

pattern_like="2017-09-18 12:47:20.50 MDT"
pattern= re.compile("\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* \\w{3} ")

g=open("sysmgr-fetched.txt","w")

def go_up(index):
    for ind in range(index,-1,-1):
        if re.match(pattern,file[ind]):
            #print file[ind]   
            return ind

def go_down(index):
    for ind in range(index,len(file)):
        if re.match(pattern,file[ind]):
            #print file[ind]
            return ind

def print_lines(ind1,ind2):
    for ind in range(ind1,ind2):
        #print file[ind]
        g.write(file[ind])
    if ind1==ind2:
        #print file[ind1]
        g.write(file[ind1])

for line in file:
    ind1=0
    ind2=0
    for word in line.lower().split():
        if word in neg:
            ind1=go_up(file.index(line))
            print line
            print word
            ind2=go_down(file.index(line))
            #print ind1,ind2
            #print file.index(line)
            print_lines(ind1,ind2)
            break
        
g.close()


