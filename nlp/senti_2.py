import os
import nltk

negative_words=[]
for word in open('negative_1_github.txt','r'):
    negative_words.append(word.strip())

folder=os.listdir('curie_logs')



negative_log_words=set()

for file in folder:
    print "open file : " +file
    for line in open("curie_logs//"+file,'r'):
        for word in nltk.word_tokenize(line.strip()):
            if word in negative_words:
                negative_log_words.add(word)
                #print word


g=open('negative_log_words.txt','w')

for word in negative_log_words:
    g.write(word+"\n")


g.close()

    
                
        
