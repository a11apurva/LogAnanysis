#import myshutil
from myshutil import copytree, ignore_patterns

dir_src = r"/home/apurva/storageLogs/curie-all-test"
dir_dst = r"/home/apurva/storageLogs/copied_files"

copytree(dir_src, dir_dst, ignore=ignore_patterns('*.ko', '*dump*','vm*','*.bz*'))

print "\n***Done Copying***\n"
