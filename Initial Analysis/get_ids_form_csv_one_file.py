import os

folder="Volume manager"

files= os.listdir("Volume manager")
ids=set()


for file in files:
    for line in open(folder+"/"+file, "r"):
        line=line.split(",")
        ids.add(line[0])


g=open(folder+"/"+folder+".txt","w")

for ele in ids:
    g.write(ele+"\n")
g.close()

        
