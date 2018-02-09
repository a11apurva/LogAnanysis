import os
import sys
import glob
import re


def convert_bytes(num):
    for x in ['b', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


dump=re.compile('dump',re.IGNORECASE)

count=0

path="gogos"

size_t=0


for root, subdirs, files in os.walk(path):

    for file in os.listdir(root):

        count+=1
        if count==1000:
            print "Processed 1K files"
            count=0
        
        filePath = os.path.join(root, file)

        if os.path.isdir(filePath):
            pass

        else:
            try:
                size=os.path.getsize(filePath)
                if re.search(dump,file):
                    size_t+=size
                    os.remove(filePath)
                    print filePath+" removed"
                    f=open(filePath+".txt",'w')
                    f.write(str(size))
                    f.close()
                else:
                    pass
            except Exception as e:
                print(e)
                continue


print "total removed : "+str(size_t)
## os.path.getsize(filePath)



'''
for root, subdirs, files in os.walk(walk_dir):
    
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    

    with open(list_file_path, 'wb') as list_file:

        for filename in files:
            file_path = os.path.join(root, filename)

            print('\t- file %s (full path: %s)\t\tsize : %s' % (filename, file_path,file_size(file_path)))
'''




'''

import os
import sys

walk_dir = "gogos"

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    print('list_file_path = ' + list_file_path)

    with open(list_file_path, 'wb') as list_file:
        for subdir in subdirs:
            print('\t- subdirectory ' + subdir)

        for filename in files:
            file_path = os.path.join(root, filename)

            print('\t- file %s (full path: %s)' % (filename, file_path))

            with open(file_path, 'rb') as f:
                f_content = f.read()
                list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
                list_file.write(f_content)
                list_file.write(b'\n')
'''
