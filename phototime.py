#! /usr/bin/python
import os
import time
import sys
pathname = sys.argv[1]
locationName = sys.argv[2]
file_extension = sys.argv[3]
file_extension_dot = ".%s"%file_extension
def rename(pathname):
    path = os.path.split(pathname)[0]
    ext = os.path.splitext(os.path.split(pathname)[1])[1]
    if ext == file_extension_dot:
        statinfo = os.stat(pathname)
        TimeStamp= time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(statinfo.st_mtime))
        os.rename(pathname,path+'/'+locationName+"_"+TimeStamp+'.%s'%file_extension)

def traverse(pathname):
    for f in os.listdir(pathname):
        if os.path.isdir(pathname+'/%s'%f) == True:
            traverse(pathname+'/%s'%f)
        else:
            rename(pathname+'/%s'%f)

traverse(pathname)