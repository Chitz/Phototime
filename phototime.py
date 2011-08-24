#! /usr/bin/python
import os
import time
import glob
import sys
pathname = sys.argv[1]
locationName = sys.argv[2]
file_extension = sys.argv[3]
def rename(pathname):
    for filename in glob.glob(os.path.join(pathname,'*.%s'%file_extension)):
        statinfo = os.stat(filename)
        TimeStamp= time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(statinfo.st_mtime))
        path = pathname + '/'
        os.rename(filename,path+locationName+"_"+TimeStamp+'.%s'%file_extension)

def traverse(pathname):
    for f in os.listdir(pathname):
        if os.path.isdir(pathname+'/%s'%f) == True:
            traverse(pathname+'/%s'%f)
        else:
            rename(pathname)

traverse(pathname)