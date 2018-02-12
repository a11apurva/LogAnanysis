import re
import os

pattern_1= re.compile("\\d{8}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} \\d{4,5}")
pattern_2= re.compile("\\d{6}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* \\d*")
pattern_3= re.compile("\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[,]?\\d* [|] ")
pattern_4= re.compile("\\w{3} \\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} \\w* ")
pattern_5= re.compile("\\d{4}[-]\\d{1,2}[-]\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} ")
pattern_6= re.compile("\\d{6}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* \\d*")

line1="20171024-06:40:50 27091 | afterFail starting |"
line2="171024-05:58:14.838 140040325277440 6,.srdata.usr.2,1,normal,1/0,24576,24576,V,0,---,N,Y"
line3="2017-10-24 06:40:35,255 | Saving any unexpected core files . . ."
line4="Apr 7 20:47:17 node1 Core_Dir=90      tpd:  All nodes panic: sdt_write_same_cont: sc=0xffff880020fa2710, vid=0x40003fffffffe sws_buff=0xffff88001d540028, data=NS Mismatch error=0x6f 0x0 Expect 0xdeeecafe 0xc03d9 0x1 0x58e84965 /dev/mapper/3600"
line5="2014-07-30 12:00:47 PDT Error       Task exited with status 1"
line6="171024-06:42:00.422 29158"

# pattern_6 taken care by pattern_2

files=os.listdir("filtered_xml")

for file in files:
    g=open("timestamp//"+file,'w')
    for line in open("filtered_xml/"+file):
        line=line.lstrip()
        if re.search(pattern_1,line): 
            g.write(re.sub(pattern_1,'',line))
        elif re.search(pattern_2,line) :
            g.write(re.sub(pattern_2,'',line))
##        elif re.search(pattern_3,line) :
##            g.write(re.sub(pattern_3,'',line))
        elif re.search(pattern_4,line) :
            g.write(re.sub(pattern_4,'',line))
        elif re.search(pattern_5,line) :
            g.write(re.sub(pattern_5,'',line))

    g.close()
