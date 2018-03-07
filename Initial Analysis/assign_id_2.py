import os

ids=set()

redundant={}

for file in os.listdir("triage"):
    ID=""
    flag=0
    f=open("triage//"+file,"r")
    for line in f:
        if "Defect Num:" in line:
            line=line.strip()
            if line=="Defect Num:":
                print file+"\t"+"H/W ERROR"
                pass
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
            if "file already exists" in str(e):
                if ID in redundant:
                    redundant[ID]+=1
                else:
                    redundant[ID]=0
                os.rename("triage//"+file,"triage//"+ID+"_"+str(redundant[ID])+".txt")

##g=open("triage_ids.txt",'w')
##for id in ids:
##    g.write(id)
##g.close()

inp=input("press any key to exist")
