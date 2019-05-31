###########################################################################################################################################
# Blink Video Downloader (BLINKDOWNLOADERB.PY)
# Credit protocol information from https://github.com/MattTW/BlinkMonitorProtocol
# Python does not Interpret TABS, change all TABS to spaces
# based on code from https://github.com/MattTW/BlinkMonitorProtocol and https://github.com/fronzbot/blinkpy
# Modifications and enhancements by John Lum (JSLSlim@gmail.com), May 27, 2019 - May 30, 2019
# To make this script work for you:
#   - Install Python 2.7.13 (other subversions of 2.7 may work) to the C: drive (unsure of necessity of this drive letter), allow installer to set environment variables
#   - Copy and paste this code into a filename ending in the .py extension
#   - change the following references (search for where these variables are declared and change the values to suit your needs):
#       - log_folder (this is where a  log of script operations/progress will be written and appended to, you must manually delete this file periodically as it will continue to grow)
#       - dir_format (change to naming convention you prefer, it is set to create/append to folders named like yyyymmdd (e.g. 20190530 for May 30, 2019)
#       - record_folder (the root folder in which all date-named folders will be created in the format defined by dir_format)
#   - Run the script from the Python root folder (where the PYTHON.EXE file is) and pass your credentials to the code
#       - Ex. PYTHON.EXE BlinkDownloaderB.py myemail@address.com MyPassword
# Notes:  You must manually delete the log file and downloaded videos periodically
#         The blink URL changes frequently.  Any change in the URL will result in a failure to download videos.  Follow the URLs above for additional info and possible updates
#         Reviewing the log file should help in troubleshooting any issues
#         This script can be called from a Task Scheduler task in Windows to download videos on a schedule
#         This code has been tested with Windows 10 Professional, Python 2.7.13 (x64), using multiple Blink XT cameras attached to a single Blink storage account, running from North America

import requests
import shutil
import os
import sys
import json
import time
import datetime
from datetime import datetime
import pytz
import os.path

# get current datetime
now = datetime.now()

# set log file location (use os.sep for os-specific path separator
log_folder = os.path.join("d:" + os.sep, "record")
# if log file exists then append, else create new
if os.path.isfile(os.path.join(log_folder, "BlinkDownloadLog.txt")):
    file=open(os.path.join(log_folder, "BlinkDownloadLog.txt"), "a")
else:
    file=open(os.path.join(log_folder, "BlinkDownloadLog.txt"), "w")
    
# write log file header info to file
file.write("Starting Blink Downloader ("+ os.path.basename(sys.argv[0]) +") at " + str(now) + "\r\n")

if len(sys.argv) != 3:
    print('usage: ' + sys.argv[0] + ' email password')
    exit()

# query Amazon for data
headers = {
    'Host': 'prod.immedia-semi.com',
    'Content-Type': 'application/json',
}

# pass credentials to Amazon
data = '{ "password" : "' + sys.argv[2] + '", "client_specifier" : "iPhone 9.2 | 2.2 | 222", "email" : "' + sys.argv[1] + '" }'
res = requests.post('https://rest.prod.immedia-semi.com/login', headers=headers, data=data)
authToken = res.json()["authtoken"]["authtoken"]

# query Amazon for region code
region = res.json()["region"]
region = list(region.keys())[0]

print("Region - " + region)
print("AuthToken - " + authToken)

headers = {
    'Host': 'prod.immedia-semi.com',
    'TOKEN_AUTH': authToken,
}

network = res.json()["networks"]

# query Amazon for account number (this is static based on your logon)
accountID = list(network.keys())[0]
print("Account - " + accountID)

# Write header info to file
now = datetime.now()
file.write(str(now) + ": Region: " + region + "; AuthToken: " + authToken + "; AccountID: " + accountID + "\r\n")

# set different representation masks for date
fileFormat = "%Y-%m-%d %H-%M-%S"
dirFormat = "%Y%m%d"

# initialize page number for querying Amazon
pageNum = 1  # Page actually appear to start at one
while True:
    # slow requests to Amazon to prevent false detection of DOS attack/lockout 
    time.sleep(0.25)    # time expressed in seconds, fractional expressions in decimal form are acceptable (e.g. 0.25 = 1/4 second)
    #pageNumUrl = 'https://rest-'+region+'.immedia-semi.com/api/v2/videos/changed?since=2016-01-01T23:11:21+0000&page=' + str(pageNum)
    # this URL changes frequently.  Check source website for updates (see top of file for web address)
    pageNumUrl = 'https://rest-'+region+'.immedia-semi.com/api/v1/accounts/'+accountID+'/media/changed?since=2019-04-19T23:11:20+0000&page=' + str(pageNum)
    print("## Processing page - " + str(pageNum) + " ##")
    res = requests.get(pageNumUrl, headers=headers)
    # retrieve list of videos (referred to now as media)
    videoListJson = res.json()["media"]
    # if list of videos is empty then quit
    if not videoListJson:
        print(" * ALL DONE !! *")
        now = datetime.now()
        file.write("======================================== END BLINKDOWNLOADER at " + str(now) + " ========================================" + "\r\n")
        file.close()
        break
        # if list contains media assets then begin processing
    for videoJson in videoListJson:
        # query datetime and format
        datetime_object = datetime.strptime(videoJson["created_at"], '%Y-%m-%dT%H:%M:%S+00:00')
        # normalize datetime to current time zone
        utcmoment = datetime_object.replace(tzinfo=pytz.utc)
        localDatetime = utcmoment.astimezone(pytz.timezone(videoJson["time_zone"]))
        # format datetime to defined mask
        dirNameNoPunc = localDatetime.strftime(dirFormat)
        record_folder = os.path.join("d:" + os.sep, "record", dirNameNoPunc)
        # if destination folder exists do nothing
        if os.path.isdir(record_folder):
            pass
        else:
            # create destination folder
            os.mkdir(record_folder)
            now = datetime.now()
            file.write(str(now) + ": Creating folder: " + record_folder + "\r\n")
        print(json.dumps(videoJson, indent=4, sort_keys=True))
        # address return example:  address = /media/u004/account/15757/network/16145/camera/41083/clip_1nQe97PJ_2019_05_14__15_18PM.mp4
        mp4Url = 'https://rest-'+region+'.immedia-semi.com' + videoJson["media"]
        print("address = " + videoJson["media"])
        file.write(str(now) + ": Original Path: " + videoJson["media"] + "\r\n")
        print("Directory: " + dirNameNoPunc)
        # define filename including unique foldername based on date in format yyyymmdd
        fileName = os.path.join(record_folder, localDatetime.strftime(fileFormat) + " - " + videoJson["device_name"] + " - " + videoJson["network_name"] + ".mp4")
        # if file already exists then skip downloading
        if os.path.isfile(fileName):
            print(" * Skipping " + fileName + " *")
            now = datetime.now()
            file.write(str(now) + ": Skipping file " + fileName + "\r\n")
            # print("Already downloaded (diff : " + str((int(videoJson["size"])-os.path.getsize(fileName))) + " bytes)")
        else:
            # download the file and rename it
            # print("Downloading - " + mp4Url)
            print("Saving - " + fileName)
            res = requests.get(mp4Url, headers=headers, stream=True)
            record_folder = os.path.join("d:" + os.sep, "record", dirNameNoPunc)
            record_tmpname = os.path.join(record_folder, "tmp-download")
            # try...except block to ignore errors when downloading
            try:
                with open(record_tmpname, 'wb') as out_file:
                    shutil.copyfileobj(res.raw, out_file)
                os.rename(record_tmpname, fileName)
                now = datetime.now()
                file.write(str(now) + ": Saving File As: " + fileName + "\r\n")
            except:
                pass
    pageNum += 1
