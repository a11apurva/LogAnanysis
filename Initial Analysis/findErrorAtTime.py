












import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import glob
import os
import string
import datetime

stop_words = set(stopwords.words('english'))
count=0

wordcount=dict()
timecount=dict()
count=0

for filename in glob.glob(os.path.join('edison_logs','*.log')):
    #print "file open: "+str(filename)
    for line in open(filename):
        line=line.strip()

        try:
            timestamp=line.split()[0].split('-')[1][:8]
            
            if timestamp=="19:00:37" :
                if 'error' in line.lower():
                    print (line)
                    count+=1

        except:
            pass
                

print (count)
