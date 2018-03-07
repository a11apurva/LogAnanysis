import os

ids=set()

for file in os.listdir("triage"):
    ID=""
    flag=0
    f=open("triage//"+file,"r")
    for line in f:
        if "Defect Num:" in line:
            line=line.strip()
            if line=="Defect Num:":
                print file+"\t"+"H/W ERROR"
            else:
                line=line.replace("Defect Num:","")
                line.strip()
                print file+"\t"+line
                #g.write(line+"\n")
                ids.add(line+"\n")
                ID=line
                flag=1
            break
    f.close()
    if flag==1:
        try:
            os.rename("triage//"+file,"triage//"+ID+".txt")
        except Exception as e:
            print e

g=open("triage_ids.txt",'w')
for id in ids:
    g.write(id)
g.close()
