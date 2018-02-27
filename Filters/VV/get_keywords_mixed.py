import re
import os


files=os.listdir("seperated_fetched_xml_VV//101-200")

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#pattern1='[+0x][a-zA-Z0-9]*$'  #'[+0x]+[a-zA-Z0-9/x]*$'
pattern2='[+]{1}[0]{1}[x]{1}[a-zA-Z0-9/x]*$'     # remove : vb_clean_thread+0x0/0x56e
pattern3='[\[]{1}[0-9\[\]/x]*$'                  # remove : lru_ws_dev_hdr[0][0]                #'[0-9\[\]/x]*$'
pattern4='\(+[A-Za-z0-9.\-&;]*\)*$'              # remove : dev_hdr(r&;u_.w)
pattern5='[=]{1}[a-zA-Z0-9\-]+$'                 # to-keep: status=-2

for file in files:
    g=open("key_words_mixed/101-200//"+file,'w')
    words=set()
    for line in open("seperated_fetched_xml_VV//101-200//"+file):

        if ("bug_id" in line) or ("short_desc" in line):
            continue
        
        line2=line.strip('\t')
        line2=line2.strip('>')
        line2=line2.strip()
        line2=line2.replace('&gt;','')
        line2=line2.replace('&lt;','')
        line2=line2.replace('&quot;','')
        line2=line2.replace('&apos;','')        
        
        line2=line2.split()

        for a in line2:
            if hasNumbers(a):
                continue
            b=a
            a=a.strip()
            a=a.replace('&gt;','')
            a=a.replace('&quot;','')
            a=a.replace('&lt;','')
            a=a.replace('&apos;','')
            a=a.replace('4&gt;','')
            a=a.strip(')|(|[|]|.|*|_|:|,|/|\\|{|}|;|$')
            if re.search(pattern2,a) :
                a=re.sub(pattern2,'',a)
            if re.search(pattern3,a):
                a=re.sub(pattern3,'',a)
            if re.search(pattern4,a):
                a=re.sub(pattern4,'',a)
            a=a.strip(')|(|[|]|.|*|_|:|,|/|\\|{|}|$')
            a=a.strip()
            if (a.islower()==False) and (a.isupper()==False) and ("_" not in a) and a.isalnum() and (a[0].isupper()==False):
                #print b+"\t"+a
                #print a
                words.add(a)

    for a in words:
        g.write(a+"\n")
                
    g.close()

        
        
   
