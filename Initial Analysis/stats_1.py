import os



line_c=[]
file_c=[]
text_c=[]
log_c=[]
mon_c=[]
error_c=[]
fail_c=[]

folders=['141_DEVEL', '174_3046_20170119.005507_DEVEL', '192_20170223.164110_DEVEL', '197_DEVEL', '212', '215_3039_20170510.163758_GA_SCSI', '215_3086_20170421.181251', '215_3086_20170512.180812', '215_3086_20170517.182232', '215_3086_20170523.181626', '215_3086_20170524.181146', '215_3086_20170606.181620', '265_20170908.103807_MU1', '279_20170905.094627_MU2', '279_20170919.133742_MU2', '279_MU2', '296_20171004.123110_MU2', '2_20160217.174255_DEVEL', '2_3046_20160219.182312_DEVEL', '2_DEVEL', '34_DEVEL', '4_2000_20160220.163740_GA_PERF', '4_3054_20160226.170308_GA_COMPRESS', '4_3054_20160229.164543_GA_COMPRESS', '4_3054_20160302.161638_GA_COMPRESS', '4_3054_20160304.165633_GA_COMPRESS', '64_20160524.060030_DEVEL', '6_DEVEL']
folders=['curie-all']

for folder in folders:
    path=r""+folder
    print path

    line_count=0
    file_count=0
    text_count=0
    log_count=0
    mon_count=0
    error_count=0
    fail_count=0
    
    for root, subdirs, files in os.walk(path):

        for file in os.listdir(root):
            
            filePath = os.path.join(root, file)

            if os.path.isdir(filePath):
                pass
            else:
                file_count+=1
                if file.endswith(".txt"):
                    text_count+=1
                elif file.endswith(".log"):
                    log_count+=1
                elif file.endswith(".mon"):
                    mon_count+=1
                
                try:
                    for line in open(filePath,"r"):
                        line_count+=1
                        if "error" in line.lower():
                            error_count+=1
                        if "fail" in line.lower():
                            fail_count+=1
                except Exception as e:
                    print str(e)
                    continue

    print "updating"        
    line_c.append(line_count)
    file_c.append(file_count)
    text_c.append(text_count)
    log_c.append(log_count)
    mon_c.append(mon_count)
    error_c.append(error_count)
    fail_c.append(fail_count)
          
print ("\n\n") 
print ("Total files : \t"+ str( sum(file_c)/len(file_c) ))
print ("Total .txt files : \t"+ str( sum(text_c)/len(text_c) ))
print ("Total .log files : \t"+ str( sum(log_c)/len(log_c) ))
print ("Total .mon Files : \t"+ str( sum(mon_c)/len(mon_c) ))
print ("Total line count : \t"+ str( sum(line_c)/len(line_c) ))
print ("Total error count : \t"+ str(sum(error_c)/len(error_c) ))
print ("Total fail count : \t"+ str( sum(fail_c)/len(fail_c) ))
