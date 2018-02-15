from myshutil import copyfile
#copyfile(src, dst)

f=open("E:\chandru\honda.log","r")
path=[]
for line in f:
    path.append("Z:\\"+(line.strip()).replace('/','\\'))
f.close()
    
count=1

for line in path:
    src=line
    dst="E:\\chandru\\triage\\" + str(count)+".txt"
    copyfile(src, dst)
    if count % 100 == 0 :
        print count 
    count+=1
    
print "\n***Done Copying***\n"
