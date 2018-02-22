import os
import nltk

negative_words=[]
for word in open('negative_1_github.txt','r'):
    negative_words.append(word.strip())

folder=os.listdir('curie_logs')

g=open('negative_1_github.txt','r')

for file in folder:
    for line in open("curie_logs//"+file,'r'):
        for word in nltk.word_tokenize(line.strip()):
            if word in negative_words:
                g.write(word+"\n")
                print word

g.close()

    
                
        
