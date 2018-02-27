import os

files=os.listdir("training")


for file in files:

    f=open("cleaned//"+file,'w')
    print file
    for line in open("training//"+file,'r'):
        if (line=="\n"):# or ("Defect Num:" in line) or ("Defect Num:" in line) or ("*****" in line):
            continue
        line2=line.strip()    
        line2=line2.strip('>')
        line2=line2.strip()
        line2=line2.replace('&gt;','')
        line2=line2.replace('&lt;','')
        line2=line2.replace('&quot;','')
        line2=line2.replace('&apos;','')        
        line2=line2.split()
        sentence=[]
        for a in line2:
            try:
                a.encode('utf-8').strip()
            except:
                continue
            b=a
            a=a.strip()
            a=a.replace('&gt;','')
            a=a.replace('&quot;','')
            a=a.replace('&lt;','')
            a=a.replace('&apos;','')
            a=a.replace('4&gt;','')
            a=a.strip(')|(|[|]|.|*|_|:|,|/|\\|{|}|;|-') #added -
            a.strip()
            if a=="" or len(a)<=2:
                continue
            sentence.append(a)
        if a!=[]:
            #print sentence
            f.write(" ".join(sentence)+"\n")

f.close()
