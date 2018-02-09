import os
import sys
import glob


#path="C:\Projects\logs"
path="Z:"


count=0
f=open("bugID.txt","w")

for root, subdirs, files in os.walk(path):

    for file in os.listdir(root):

        count+=1
        if count%1000 == 0:
            print "1K files processed"
            count=0
            
        filePath = os.path.join(root, file)

        if os.path.isdir(filePath):
            pass

        else:
            if file=="triage.txt":
                for line in open(filePath):
                    if "Defect Num:" in line:
                        strx= filePath
                        #print filePath
                        #print line.split()
                        try:
                            strx=strx+"\t"+line.split()[2]
                        except:
                            strx=strx+"\tNA"
                        print strx
                        f.write(strx+"\n")
                        break

f.close()
            




