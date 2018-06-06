import os
import string

path="VolumeManagerBugs - 2"

count=0
sub_folder=0
sub_sub_folder=0

for folder in os.listdir(path):
    sub_folder+=1
    sub_sub_folder=len(os.listdir(os.path.join(path,folder)))
    count+=sub_sub_folder
    print folder + "\t" + str(sub_sub_folder)

print ("\nTotal sub-folders: "+str(sub_folder))
print ("\nTotal sub-sub-folders: "+str(count))
                
            
