# A simple example to demonstrate the protocol:
# Download available videos
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
    'Host': 'rest-prod.immedia-semi.com',
    'Content-Type': 'application/json',
}
data = '{ "password" : "' + sys.argv[2] + '", "email" : "' + sys.argv[1] + '" }'
res = requests.post('https://rest-prod.immedia-semi.com/api/v4/account/login', headers=headers, data=data)
authToken = res.json()["authtoken"]["authtoken"]
region = res.json()["region"]["tier"]
accountID = res.json()["account"]["id"]

print("Region: %s AuthToken: %s Account ID: %i" % (region, authToken, accountID))

host = 'rest-%s.immedia-semi.com' % region
headers = {
    'Host': host,
    'TOKEN_AUTH': authToken,
}

res = requests.get('https://%s/api/v3/accounts/%i/homescreen' % (host,accountID), headers=headers)
networkID = str(res.json()["networks"][0]["id"])

print("Network - %s" % networkID)

fileFormat = "%Y-%m-%d %H-%M-%S"
pageNum = 1
while True:
    time.sleep(0.25)
    pageNumUrl = 'https://%s/api/v1/accounts/%i/media/changed?since=2019-04-19T23:11:20+0000&page=%i' % (host,accountID, pageNum)
    print("## Processing page - %i ##" % pageNum)
    res = requests.get(pageNumUrl, headers=headers)
    videoListJson = res.json()["media"]
    if not videoListJson:
        print(" * ALL DONE !! *")
        break
    for videoJson in videoListJson:
        # print(json.dumps(videoJson, indent=4, sort_keys=True))
        mp4Url = 'https://%s%s' % (host, videoJson["media"])
        datetime_object = datetime.strptime(videoJson["created_at"], '%Y-%m-%dT%H:%M:%S+00:00')
        utcmoment = datetime_object.replace(tzinfo=pytz.utc)
        localDatetime = utcmoment.astimezone(pytz.timezone(videoJson["time_zone"]))
        fileName = localDatetime.strftime(fileFormat) + " - " + videoJson["device_name"] + " - " + videoJson["network_name"] + ".mp4"

        if os.path.isfile(fileName):
            print(" * Skipping %s *" % fileName)
        else:
            print("Saving - %s" %fileName)
            res = requests.get(mp4Url, headers=headers, stream=True)
            with open("tmp-download", 'wb') as out_file:
                shutil.copyfileobj(res.raw, out_file)
            os.rename("tmp-download", fileName)
    pageNum += 1
