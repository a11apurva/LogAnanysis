import re
import os

pattern_1= re.compile("\\d{8}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} \\d{4,5}")
pattern_2= re.compile("\\d{6}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* \\d*")
pattern_3= re.compile("\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[,]?\\d* [|] ")
pattern_4= re.compile("\\w{3} \\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} \\w* ")
pattern_5= re.compile("\\d{4}[-]\\d{1,2}[-]\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} ")
pattern_6= re.compile("\\d{6}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* \\d*")
pattern_7= re.compile("\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} \\w{3} ")
pattern_8= re.compile("\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* ")

line1="20171024-06:40:50 27091 | afterFail starting |"
line2="171024-05:58:14.838 140040325277440 6,.srdata.usr.2,1,normal,1/0,24576,24576,V,0,---,N,Y"
line3="2017-10-24 06:40:35,255 | Saving any unexpected core files . . ."
line4="Apr 7 20:47:17 node1 Core_Dir=90      tpd:  All nodes panic: sdt_write_same_cont: sc=0xffff880020fa2710, vid=0x40003fffffffe sws_buff=0xffff88001d540028, data=NS Mismatch error=0x6f 0x0 Expect 0xdeeecafe 0xc03d9 0x1 0x58e84965 /dev/mapper/3600"
line5="2014-07-30 12:00:47 PDT Error       Task exited with status 1"
line6="171024-06:42:00.422 29158"
line7="2016-04-24 10:20:23 PDT Created     task."
line8="2010-08-30 15:24:12.02 new system log format"

# pattern_6 taken care by pattern_2

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


files=os.listdir("seperated_fetched_xml_VV/11-30")

for file in files:
    g=open("time_stamp_removed//"+file,'w')
    added=[]
    for line in open("seperated_fetched_xml_VV/11-30/"+file):
        flag=0
        line=line.lstrip('\t')
        line=line.lstrip('>')
        line=line.lstrip('&gt;')
        line=line.lstrip()
        if re.match(pattern_1,line): 
            line=re.sub(pattern_1,'',line)
            flag=1
        elif re.match(pattern_7,line) :
            line=re.sub(pattern_7,'',line)
            print line
            flag=1
        elif re.match(pattern_2,line) :
            line=re.sub(pattern_2,'',line)
            flag=1
##        elif re.search(pattern_3,line) :
##            g.write(re.sub(pattern_3,'',line))
        elif re.match(pattern_4,line) :
            line=re.sub(pattern_4,'',line)
            flag=1
        elif re.match(pattern_5,line) :
            line=re.sub(pattern_5,'',line)
            flag=1
        elif re.match(pattern_8,line) :
            line=re.sub(pattern_8,'',line)
            flag=1

        if flag==1:
            remainder=[]
            for word in line.split():
                if hasNumbers(word)==False:
                    remainder.append(word)
##                if word.isalpha:
##                    remainder.append(word)
            line=" ".join(remainder)
            if line not in added:
                if len(line.split())>2:
                    added.append(line)
                    line+="\n"
                    g.write(line)
                
    g.close()
