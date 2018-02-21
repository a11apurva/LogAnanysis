import re
import os


list1=[]

file1='11-30.txt'
file2='31-50.txt'

for id in open(file1,'r'):
    list1.append(id.strip())

g=open('temp.txt','w')
for id in open(file2,'r'):
    if id.strip() in list1:
        print id
    else:
        g.write(id)

g.close()
os.remove(file2)
os.rename('temp.txt',file2)
