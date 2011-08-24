#! /usr/bin/python
import os
import time
import glob
import sys
pathname = sys.argv[1]
locationName = sys.argv[2]
file_extension = sys.argv[3]
def change(pathname):
    for filename in glob.glob(os.path.join(pathname,'*.%s'%file_extension)):
        createdTime_Epoch = os.path.getmtime(filename)
        dateNtime = time.localtime(createdTime_Epoch)
        Day = dateNtime.tm_mday
        Month = dateNtime.tm_mon
        Year = dateNtime.tm_year
        Hour = dateNtime.tm_hour
        Min = dateNtime.tm_min
        Sec = dateNtime.tm_sec
        CreatedTime = str(Hour)+":"+str(Min)+":"+str(Sec)
        CreatedDate = str(Day) + '-' +str(Month) + '-' +str(Year)
        TimeStamp = CreatedDate+"_"+CreatedTime
        path = pathname + '/'
        os.rename(filename,path+locationName+"_"+TimeStamp+'.%s'%file_extension)

def get_file(pathname):
    for f in os.listdir(pathname):
        if os.path.isdir(pathname+'/%s'%f) == True:
            get_file(pathname+'/%s'%f)
        else:
            change(pathname)

get_file(pathname)