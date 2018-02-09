import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import glob
import os
import string

stop_words = set(stopwords.words('english'))
count=0

wordcount=dict()
timecount=dict()


for filename in glob.glob(os.path.join('hertz_logs','*.log')):
    #print "file open: "+str(filename)
    for line in open(filename):
        line=line.strip()

        if 'TermError' in line:
            print line
