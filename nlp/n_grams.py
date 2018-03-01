import os
import nltk

negative_words=[]
for word in open('NegativeWords.txt','r'):
    negative_words.append(word.strip())

n=input("input value of n : ")

path=r"C:\Projects\Log Analysis\scraper\LOGS\Volume_Manager-VV\All-vv-cleaned"

files=os.listdir(path)

for file in files:
    g=open(r"C:\Projects\Log Analysis\scraper\LOGS\Volume_Manager-VV\All-vv-cleaned-n_grams\\"+file,'w')
    for line in open(path+"\\"+file,'r'):
        line=line.strip().split()

        for word in line:
            if word in negative_words:
                #print word
                #print line
                index = line.index(word)
                l_index= (index-n) if  ((index-n)>=0) else 0
                r_index= (index+n) if  ((index+n)< len(line)) else (len(line)-1)
                strx=" ".join(line[l_index:r_index+1]) + "\n"
                #print strx
                g.write(strx)

    g.close()
                
