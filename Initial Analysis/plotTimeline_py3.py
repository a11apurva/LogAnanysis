import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import glob
import os
import string
import datetime
import matplotlib.pylab as plt
import matplotlib.pyplot as plt2

stop_words = set(stopwords.words('english'))
count=0

wordcount=dict()
timecount=dict()

system_name='edison_logs'


for filename in glob.glob(os.path.join(system_name,'*.log')):
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
                



print ("\ntime count :\n")
count=0
for k,v in sorted(timecount.items(), key=lambda p:p[1], reverse=True):
    print(k,v)
    count+=1
    if count==5:
        break




lists = sorted(timecount.items()) 

x, y = zip(*lists) 

plt2.plot(x, y)
#plt2.show()

fig = plt2.gcf()
fig.set_size_inches(18.5, 10.5, forward=True)
fig.suptitle(system_name, fontsize=20, fontweight='bold')
fig_name=system_name+".png"
fig.savefig(fig_name, dpi=100, bbox_inches='tight')