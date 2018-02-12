import re
import os


files=os.listdir("timestamp")

for file in files:
    g=open("sub-filter-1//"+file,'w')
    for line in open("timestamp//"+file):
        line2=line.lstrip('\t')
        line2=line.lstrip('>')
        line2=line.lstrip()
        
        line2=line.split()

        if len(line2) <= 2:
            continue
        elif "LOGFILEMGR" in line:
            continue
        elif "Could not complete task".lower() in line.lower():
            continue

        g.write(line)
        
    g.close()
