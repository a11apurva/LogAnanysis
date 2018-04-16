import os
import string

path="VolumeManagerBugs"

count=0

for root, subdirs, files in os.walk(path):

    for file in os.listdir(root):

        filePath = os.path.join(root, file)

        if os.path.isdir(filePath):
            pass
        else:
            if "corpus_5" not in file:
                os.remove(filePath)
                #print file

            count+=1
            if count % 100 :
                print "processed 100 files .. "
                
            
