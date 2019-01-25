# Credit protocol information from https://github.com/MattTW/BlinkMonitorProtocol

import requests
import shutil
import os
import sys
import json

from datetime import datetime
import pytz

import os.path

if len(sys.argv) != 3:
    print('usage: ' + sys.argv[0] + ' email password')
    exit()

headers = {
    'Host': 'prod.immedia-semi.com',
    'Content-Type': 'application/json',
}
data = '{ "password" : "' + sys.argv[2] + '", "client_specifier" : "iPhone 9.2 | 2.2 | 222", "email" : "' + sys.argv[1] + '" }'
res = requests.post('https://rest.prod.immedia-semi.com/login', headers=headers, data=data)
authToken = res.json()["authtoken"]["authtoken"]
region = res.json()["region"]
region = list(region.keys())[0]

print(region)
print(authToken)

headers = {
    'Host': 'prod.immedia-semi.com',
    'TOKEN_AUTH': authToken,
}

fileFormat = "%Y-%m-%d %H-%M-%S"
pageNum = 1  # Page actually appear to start at one
while True:
    pageNumUrl = 'https://rest-'+region+'.immedia-semi.com/api/v2/videos/changed?since=2016-01-01T23:11:21+0000&page=' + str(pageNum)
    print("## Processing page - " + str(pageNum) + " ##")
    res = requests.get(pageNumUrl, headers=headers)
    videoListJson = res.json()["videos"]
    if not videoListJson:
        print(" * ALL DONE !! *")
        break
    for videoJson in videoListJson:
        # print(json.dumps(videoJson, indent=4, sort_keys=True))
        mp4Url = 'https://rest-'+region+'.immedia-semi.com' + videoJson["address"]
        datetime_object = datetime.strptime(videoJson["created_at"], '%Y-%m-%dT%H:%M:%S+00:00')
        utcmoment = datetime_object.replace(tzinfo=pytz.utc)
        localDatetime = utcmoment.astimezone(pytz.timezone(videoJson["time_zone"]))
        fileName = localDatetime.strftime(fileFormat) + " - " + videoJson["camera_name"] + " - " + videoJson["network_name"] + ".mp4"

        if os.path.isfile(fileName):
            print(" * Skipping " + fileName + " *")
            # print("Already downloaded (diff : " + str((int(videoJson["size"])-os.path.getsize(fileName))) + " bytes)")
        else:
            # print("Downloading - " + mp4Url)
            print("Saving - " + fileName)
            res = requests.get(mp4Url, headers=headers, stream=True)
            with open("tmp-download", 'wb') as out_file:
                shutil.copyfileobj(res.raw, out_file)
            os.rename("tmp-download", fileName)
    pageNum += 1
