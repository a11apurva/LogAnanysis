import os


files= os.listdir("Products")

for file in files:
    g=open(file.replace(".csv",".txt"),"w")
    for line in open("Products/"+file, "r"):
        line=line.split(",")
        g.write(line[0]+"\n")
    g.close()

        
