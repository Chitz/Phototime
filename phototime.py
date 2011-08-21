import sys
import os, time
import subprocess

path = sys.argv[1]
ftype = "/*." + sys.argv[2]	# I can't believe I was too lazy to add this line before ;)
# os.listdir(path) Add this for nested directories later + 
filelist = subprocess.Popen("ls " + path + ftype , shell=True,stdout=subprocess.PIPE, cwd=None).stdout.read().strip('\n').split('\n')
for i in filelist:
	statinfo = os.stat(i)
	newname= time.strftime("%Y-%m-%d %H.%M:%S", time.localtime(statinfo.st_mtime)) + ".%s"%(sys.argv[2])
	os.renames(i,path+"/"+newname)



