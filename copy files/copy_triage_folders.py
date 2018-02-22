import myshutil
from myshutil import copytree, ignore_patterns
import os


folders=[]
for line in open('triage_path_test.txt','r'):
    line=line.strip()
    line=line.replace('\\triage.txt','')
    folders.append(line)

#folders=[r'E:\chandru\copied\3.2.3\100_DEVEL\eagles\testsrc_SysmgrTests_TuneSysmgrFailover-151022-233538\logs']

for foldername in folders:
    try:
        dir_src = os.path.join(r"",foldername)
        dir_dst = os.path.join(r"E:\chandru\NEW",foldername.replace("E:\chandru\\",""))

        copytree(dir_src, dir_dst)

        print "copied folder : "+foldername
        
    except Exception as e:
        print(e)
        continue

print "\n***Done Copying***\n"

