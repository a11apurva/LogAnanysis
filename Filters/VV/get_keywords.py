import re
import os


files=os.listdir("seperated_fetched_xml_VV//1-10")

for file in files:
    g=open("key_words//"+file,'w')
    for line in open("seperated_fetched_xml_VV//1-10//"+file):

        if ("bug_id" in line) or ("short_desc" in line):
            continue
        
        line2=line.strip('\t')
        line2=line2.strip('>')
        line2=line2.strip()
        line2=line2.strip('&gt;')
        line2=line2.strip('&lt;')
        line2=line2.strip('&quot;')
        line2=line2.strip('&apos;')        
        
        line2=line2.split()

        for a in line2:
            a=a.strip()
            a=a.strip('&gt;')
            a=a.strip('&quot;')
            a=a.strip('&lt;')
            a=a.strip('&apos;')
            a=a.replace('4&gt;','')
            a=a.strip(')|(|[|]')
            a=a.strip(':|,')
            a=a.strip()
            if a.islower() and "_" in a:
                print a
                g.write(a+"\n")

    g.close()

        
        
   
