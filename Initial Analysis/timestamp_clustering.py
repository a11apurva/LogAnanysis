import os
import re

folder='curie_logs'

files=os.listdir(folder)

pattern_1= re.compile("\\d{8}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} \\d{4,5}")
pattern_2= re.compile("\\d{6}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* \\d*")
pattern_3= re.compile("\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[,]?\\d*")
pattern_4= re.compile("\\w{3} \\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} \\w* ")
pattern_5= re.compile("\\d{4}[-]\\d{1,2}[-]\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} ")
pattern_6= re.compile("\\d{6}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* \\d*")
pattern_7= re.compile("\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} \\w{3} ")
pattern_8= re.compile("\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* ")
pattern_9= re.compile("\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* \\w{3} ")

line1="20171024-06:40:50 27091 | afterFail starting |"
line2="171024-05:58:14.838 140040325277440 6,.srdata.usr.2,1,normal,1/0,24576,24576,V,0,---,N,Y"
line3="2017-10-24 06:40:35,255 | Saving any unexpected core files . . ."
line4="Apr 7 20:47:17 node1 Core_Dir=90      tpd:  All nodes panic: sdt_write_same_cont: sc=0xffff880020fa2710, vid=0x40003fffffffe sws_buff=0xffff88001d540028, data=NS Mismatch error=0x6f 0x0 Expect 0xdeeecafe 0xc03d9 0x1 0x58e84965 /dev/mapper/3600"
line5="2014-07-30 12:00:47 PDT Error       Task exited with status 1"
line6="171024-06:42:00.422 29158"
line7="2016-04-24 10:20:23 PDT Created     task."
line8="2010-08-30 15:24:12.02 new system log format"
line9="2009-08-13 18:07:04.24 PDT {6729} {events:normal       }"

# pattern_6 taken care by pattern_2

dict1={pattern_1:['***20171024-06:40:50 27091***'],pattern_2:['***171024-05:58:14.838 140040325277440***'],
       pattern_3:['***2017-10-24 06:40:35,255***'],pattern_4:['***Apr 7 20:47:17 node1***'],
       pattern_6:['***171024-06:42:00.422 29158***'],
       pattern_7:['***2016-04-24 10:20:23 PDT***'],pattern_8:['***2009-08-13 18:07:04.24 PDT***'],
       pattern_9:['***No Pattern***']}

for file in files:
    f=open(folder+"//"+file,'r')
    line=f.readline()
    f.close()
    

    line=line.lstrip('\t')
    line=line.lstrip('>')
    line=line.lstrip('&gt;')
    line=line.lstrip()
    if re.match(pattern_9,line): 
        print file+"\tpattern_9\t"+line
        dict1[pattern_9].append(file)
    if re.match(pattern_1,line): 
        print file+"\tpattern_1\t"+line
        dict1[pattern_1].append(file)
    elif re.match(pattern_7,line) :
        print file+"\tpattern_7\t"+line
        dict1[pattern_7].append(file)
    elif re.match(pattern_2,line) :
        print file+"\tpattern_2\t"+line
        dict1[pattern_2].append(file)
    elif re.search(pattern_3,line) :
        print file+"\tpattern_3\t"+line
        dict1[pattern_3].append(file)
    elif re.match(pattern_4,line) :
        print file+"\tpattern_4\t"+line
        dict1[pattern_4].append(file)
##    elif re.match(pattern_5,line) :
##        print file+"\tpattern_5\t"+line
##        dict1[pattern_5].append(file)
    elif re.match(pattern_8,line) :
        print file+"\tpattern_8\t"+line
        dict1[pattern_8].append(file)
    else:
        print file+"\tNO_PATTERN\t"+line
        dict1[pattern_9].append(file+"\t::\t"+line)

    
                
f=open('timestamp_clustering_v.txt','w')
for key in dict1:
    f.write("\n\n")
    for val in dict1[key]:
        print val
        f.write(val+"\n")
f.close()













    
