import os

folders=['curie-all']


unique=set()
g=open("sysmgr_logging.txt","w")

for folder in folders:
    path=r""+folder
    print path
    
    for root, subdirs, files in os.walk(path):

        for file in os.listdir(root):
            
            filePath = os.path.join(root, file)

            if os.path.isdir(filePath):
                pass
            else:
                try:
                    if file=="sysmgr":
                        g.write(filePath+"\n")
                        for line in open(filePath,"r"):
                            line=line.split()
                            #print line
                            if len(line)>4:
                                #print line
                                line=line[4].strip()
                                line=line.strip('{|}')
                                line=line.strip()
                                unique.add(line)
                                #print line
                except Exception as e:
                    print e

g.close()

g=open("sysmgr_unique.txt","w")

for ele in unique:
    g.write(ele+"\n")

g.close()
                    
