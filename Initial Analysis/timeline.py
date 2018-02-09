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


for filename in glob.glob(os.path.join('hertz_logs','*.log')):
    #print "file open: "+str(filename)
    for line in open(filename):
        line=line.strip()

        try:
            timestamp=line.split()[0].split('-')[1][:8]
            timestamp = datetime.datetime.strptime(timestamp, "%H:%M:%S")

            if timestamp not in timecount:
                timecount[timestamp] = 1
            else:
                timecount[timestamp] += 1

        except:
            pass
                



print "\ntime count :\n"
count=0
for key, value in sorted(timecount.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)
    count+=1
    if count==5:
        break




