import re
import os

pattern_1= re.compile("\\d{8}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} \\d{5}")
pattern_2= re.compile("\\d{6}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* \\d*")
pattern_3= re.compile("\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[,]?\\d* [|] ")
pattern_4= re.compile("\\w{3} \\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} \\w* ")
pattern_5= re.compile("\\d{4}[-]\\d{1,2}[-]\\d{1,2} \\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2} ")
pattern_6= re.compile("\\d{6}[-]?\\d{1,2}[:]?\\d{1,2}[:]?\\d{1,2}[.]?\\d* \\d*")
# pattern_6 taken care by pattern_2

commands=[]
for line in open('commands.txt','r'):
    commands.append(line.strip())


files=os.listdir("filtered_xml")

for file in files:
    g=open("command-logs//"+file,'w')
    for line in open("filtered_xml/"+file):
        line=line.lstrip()
        line=line.lower()

        for ele in commands:
            if ele in line:
                if re.search(pattern_1,line): 
                    g.write(re.sub(pattern_1,'',line))
                elif re.search(pattern_2,line) :
                    g.write(re.sub(pattern_2,'',line))
                elif re.search(pattern_3,line) :
                    g.write(re.sub(pattern_3,'',line))
                elif re.search(pattern_4,line) :
                    g.write(re.sub(pattern_4,'',line))
                elif re.search(pattern_5,line) :
                    g.write(re.sub(pattern_5,'',line))
                else:
                    g.write(line)
                break

    g.close()


