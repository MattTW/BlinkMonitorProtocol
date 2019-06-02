# Credit protocol information from https://github.com/MattTW/BlinkMonitorProtocol

import requests
import shutil
import os
import sys
import json
import time

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

network = res.json()["networks"]
accountID = list(network.keys())[0]
print("Account - " + accountID)

fileFormat = "%Y-%m-%d %H-%M-%S"
pageNum = 1
while True:
    time.sleep(0.25)
    pageNumUrl = 'https://rest-'+region+'.immedia-semi.com/api/v1/accounts/'+accountID+'/media/changed?since=2019-04-19T23:11:20+0000&page=' + str(pageNum)
    print("## Processing page - " + str(pageNum) + " ##")
    res = requests.get(pageNumUrl, headers=headers)
    videoListJson = res.json()["media"]
    if not videoListJson:
        print(" * ALL DONE !! *")
        break
    for videoJson in videoListJson:
        # print(json.dumps(videoJson, indent=4, sort_keys=True))
        mp4Url = 'https://rest-'+region+'.immedia-semi.com' + videoJson["media"]
        datetime_object = datetime.strptime(videoJson["created_at"], '%Y-%m-%dT%H:%M:%S+00:00')
        utcmoment = datetime_object.replace(tzinfo=pytz.utc)
        localDatetime = utcmoment.astimezone(pytz.timezone(videoJson["time_zone"]))
        fileName = localDatetime.strftime(fileFormat) + " - " + videoJson["device_name"] + " - " + videoJson["network_name"] + ".mp4"

        if os.path.isfile(fileName):
            print(" * Skipping " + fileName + " *")
        else:
            print("Saving - " + fileName)
            res = requests.get(mp4Url, headers=headers, stream=True)
            with open("tmp-download", 'wb') as out_file:
                shutil.copyfileobj(res.raw, out_file)
            os.rename("tmp-download", fileName)
    pageNum += 1
