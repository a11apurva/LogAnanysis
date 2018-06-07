import os

g=open("hashed-volMgr.txt","w")

path="../VolumeManagerBugs-top"

index=["A","B","C","D","E","F","G","H","I","J"]

def hash_string(line):
    order=0
    
    for char in line:
        order+=ord(char)

    order=str(order)

    hash_str=""

    for ch in order:
        hash_str+=index[int(ch)]

    return hash_str


for root, subdirs, files in os.walk(path):

    for file in os.listdir(root):

        filePath = os.path.join(root, file)

        if "corpus_3_4_no_num_no_english" not in file:
            continue

        doc=""

        for line in open(filePath,"r"):
            line=line.strip()
            line=line.replace(" ","")
            
            hash_str = hash_string(line)

            doc=doc + (hash_str+" ")

        label="__label__"+filePath.split("\\")[-3]+" "
        line=label+doc
        if line==label:
            continue
        g.write(line.rstrip()+"\n")    
    
    
